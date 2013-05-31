import maya.cmds as cmds
import os


class Test_UI2:
    def __init__(self):
        
        self.UIElements = {}
        
        """ This dictionary will be used to store the names of your blueprints. """
        self.blueprints = {}
        
        """ Here we call on a function that will find the contents of the Layout folder. """
        """ Those contents are added to the dictionary """
        self.blueprints['Layout'] = self.findAllModules("System/Widgets/Layout")
        """ Print the self.blueprints['Layout'] """
        print self.blueprints['Layout']
        
        
        wHeight = 100
        wWidth = 400
        
        bHeight = 20
        
        if cmds.window("layout_UI_window", exists = True):
            cmds.deleteUI("layout_UI_window")
            
        self.UIElements["window"] = cmds.window("layout_UI_window", width = wWidth, height = wHeight)
        
        self.UIElements['flowLayout'] = cmds.flowLayout(visible=True, columnSpacing=5, w=wWidth, h=wHeight, v=True, p=self.UIElements["window"])
        
        cmds.setParent(self.UIElements['flowLayout'])

        cmds.separator()

          
        cmds.showWindow("layout_UI_window")
        
        
    def findAllModules(self, relativeDirectory, *args):
        
        # search the relative directory  for all available modules
        # Return a list of all module names (excluding the ".py" extension)
        fileDirectory = os.environ["RIGTOOL"] + "/" + relativeDirectory + "/"
        
        allPyFiles = self.findAllFiles(relativeDirectory, fileDirectory, ".py")
        
        returnModules = []
        
        for file in allPyFiles:
            if file != "__init__":
                returnModules.append(file)
                
        return returnModules
    
    def findAllFiles(self, relativeDirectory, fileDirectory, fileExtension):
        # Search the relative directory for all files with the given extension.
        # Return a list of all file names, excluding the file extension
 
        allFiles = os.listdir(fileDirectory)
        
        # Refine all files, listing only those of the specified file extension
        returnFiles = []
        for f in allFiles:
            splitString = str(f).rpartition(fileExtension)
            
            if not splitString[1] == "" and splitString[2] == "":
                returnFiles.append(splitString[0])
    
        return returnFiles