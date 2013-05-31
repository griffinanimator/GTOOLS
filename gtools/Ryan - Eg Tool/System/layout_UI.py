import maya.cmds as cmds
import os
import sys
import csv

class Layout_UI:
    def __init__(self):
        
        self.UIElements = {}
        self.widgets = []
        
        """ I put this in to demonstrate how you could make a widget for various layout modules. """
        """ This is not hooked up to anything """
        ############################################################
        riggingToolRoot = os.environ["RIGTOOL"]
        self.path = "R:/System/CSV_files/armCsv.csv"

        lytWidgets = os.listdir(self.path)
        for widget in lytWidgets:
            prefix = 'lyt_' 
            result = widget.startswith(prefix)
            if result == True:
                self.widgets.append(widget)
                
        print self.widgets
        #########################################################

     
        wHeight = 100
        wWidth = 400
        
        bHeight = 20
        
        if cmds.window("layout_UI_window", exists = True):
            cmds.deleteUI("layout_UI_window")
            
        self.UIElements["window"] = cmds.window("layout_UI_window", width = wWidth, height = wHeight)
        
        self.UIElements['flowLayout'] = cmds.flowLayout(visible=True, columnSpacing=5, w=wWidth, h=wHeight, v=True, p=self.UIElements["window"])
        
        cmds.setParent(self.UIElements['flowLayout'])

        cmds.separator()
        cmds.text(label = "Enter Number of locators to be created")
        
        self.UIElements['numLocators'] = cmds.intField()
        
        cmds.button(label = 'Load_LYT', width =wWidth, height = bHeight, vis = True, c = self.createLocators)
        
        cmds.text(label = "Position locators, select in order and open Rig_UI")
   
        cmds.button(label = 'Rig_UI', width =wWidth, height = bHeight, vis = True, c = self.callRig_UI)
    
        cmds.showWindow("layout_UI_window")
    

    
    """ This function creates a number of locators based of user input.  I stole the idea from Sammy : ) """
    def createLocators(self, *args):
        numLoc = cmds.intField(self.UIElements['numLocators'], query = True, value = True, w = 80, h = 80, minValue = 1, maxValue = 3, step = 1)
        
        """ Define a default starting position for the locators. """
        locPos = ([-5.0, 5.0, 0.0], [0.0, 5.0, 0.0], [5.0, 5.0, 0.0])
        
        for index in range(numLoc):
            cmds.spaceLocator(n = 'lytLoc_1', p = locPos[index]) 
            
    def callRig_UI(self, *args):
        cmds.deleteUI(self.UIElements["window"])
        
        import System.rigTool_UI as rigTool_UI
        reload(rigTool_UI)
        UI = rigTool_UI.RigTool_UI()
        
            