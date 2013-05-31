""" rigTool_UI.py """
""" Ryan Griffin - 07-06-11 """
""" UI for the Auto-Rigging tool """

import maya.cmds as cmds
import os
import sys
from functools import partial

import System.utils as utils

class RigTool_UI:
    def __init__(self):
        
        self.UIElements = {}
        
        """ This dictionary will be used to store the names of your blueprints. """
        self.blueprints = {}
      
        """ UI Dimensions """
        wHeight = 400
        wWidth = 632.5
        """ Buttons' size """
        bWidth = 66
        bHeight = 66
        
        columnOffset = 5
        
        
        """ Check to see if the window exists.  If True delete it.  If False, delete it. """
        if cmds.window("garveyAUTORIG", exists=True):
            cmds.deleteUI("garveyAUTORIG")
        
        
        """ Create a window"""
        self.UIElements['window'] = cmds.window("garveyAUTORIG", width=wWidth, height=wHeight)
        
        
        """ Make a layout.  Layouts are parented to the window and hold UI elements.
        A layout organizes the element in a defined way such as lining them up in a column """
        self.UIElements["listBoxRowLayout"] = cmds.rowLayout(nc=2, columnWidth2=[400, 300], columnAttach=([1, "left", columnOffset], [2, "both", columnOffset]), rowAttach=([1, "top", columnOffset], [2, "top", columnOffset]))
        """ A flowLayout which goes into the listBoxRowLayout """
        self.UIElements['flowLayout'] = cmds.flowLayout(visible=True, columnSpacing=5, w=wWidth, h=wHeight, v=True)
        """ This sets the parent to the top level layout """
        cmds.setParent('..')

        """ Here we call on a function that will find the contents of the Layout folder. """
        """ Those contents are added to the dictionary """   
        self.blueprints['Layout'] = utils.findAllModules("System/Widgets")
        
        """ For each valid module, we make a button """
        """ I suggest splitting modules into animation and layout folders """
        for module in self.blueprints['Layout']:
            cmds.setParent(self.UIElements['flowLayout'])
            self.UIElements['rowLayout'] = cmds.rowLayout(numberOfColumns=2, columnWidth=([1, bWidth]), adjustableColumn=2, columnAttach=([1, "both", 0], [2, "both", 5]))
            cmds.setParent(self.UIElements['rowLayout'])

            buttonInfo = self.createBluprintButton(module) 
    
            if buttonInfo != None:
                """This is the button that will build your module.  1 button is created for every successfully imported module. """
                self.UIElements["module_button_"+module] = cmds.symbolButton(width=bHeight, height=bWidth, image=buttonInfo[2], command=partial(self.installBlueprint, module))  
                cmds.columnLayout(columnAlign="center") 
                cmds.text(label=buttonInfo[1])   

        """ Make a button to place in the window """
        # Commented out
        #cmds.button(label='Make Arm', width=bWidth, height=bHeight, visible=True, command=self.buildArm)
        #cmds.button(label='Make Leg', width=bWidth, height=bHeight, visible=True, command=self.buildLeg)
        #cmds.button(label='Save CSV', width=bWidth, height=bHeight, visible=True, command=self.createCSVfile)
        #cmds.button(label='Make Spine', width=bWidth, height=bHeight, visible=True)
        #cmds.button(label='Make Face', width=bWidth, height=bHeight, visible=True)
        #cmds.button(label='Make Hand', width=bWidth, height=bHeight, visible=True)
        #cmds.button(label='Make Foot/Toes', width=bWidth, height=bHeight, visible=True)
        #cmds.button(label='Create Hinge', width=bWidth, height=bHeight, visible=True, command=self.buildHinge)
        cmds.showWindow("garveyAUTORIG")

        
    def createBluprintButton(self, module, *args): 
        """ This creates a string equal to System.Widgets.(the modules name) """
        """ Import every script in "System.Widgets.".  If the script has an ICON variable, we will return the module info to the UI """
        
        mod = __import__("System.Widgets."+module, {}, {}, [module])
        reload(mod)
        
        """ Try statements just try to do something.  If it fails an exception is raised"""
        """ In this case the exception causes the function to pass and try the next loop """
        """ Look at buildHinge.  See the TITLE, DESCRIPTION, an ICON? """
        try:
            title = mod.TITLE
            description = mod.DESCRIPTION
            icon = mod.ICON
            return (title, description, icon)
     
        except: pass
        
    def installBlueprint(self, module, *args):
        """ This takes the place of your individual build functions """
        mod = __import__("System.Widgets."+module, {}, {}, [module])
        reload(mod)
        
        moduleClass = getattr(mod, mod.CLASS_NAME)
        moduleInstance = moduleClass()
        
        

    """ You could get rid of all of these other build functions """
    """ Try building another function that builds from your layout objects """

    """ Build Arm """
    def buildArm(self, *args):
        """ Instance in our build arm class so we can run it from the UI """
        import System.Widgets.buildArm as bldArm
        """ reload bldArm rather than use the compiled .pyc.  This is only needed while you are changing the code. """
        reload(bldArm)
        """Assign the Build_Arm class to a variable """
        createArm = bldArm.Build_Arm()
        """ Run the buildArm function from the Build_Arm class """
        createArm.buildArm(self, *args)
        
        
    """ Build Leg """
    def buildLeg(self, limb, side, *args):
        """ Instance in the buildLeg class """
        import System.Widgets.buildLeg as bldLeg
        #reload(bldLeg)
        createLeg = bldLeg.Build_Leg()
        createLeg.buildLeg()
        
    def buildHinge(self, *args):
        """ Instance in the Build Hinge class """
        import System.Widgets.buildHinge as buildHinge
        reload (buildHinge)
        createHinge = buildHinge.Hinge()
        createHinge.buildHinge()