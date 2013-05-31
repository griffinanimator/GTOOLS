import maya.cmds as cmds
import os
import sys

class Directory_Utils:
    def __init__(self, riggingToolRoot):
        self.riggingToolRoot = riggingToolRoot
        self.dirs = {}
        
        self.getBlueprintObject()
    
    def getBlueprintObject(self):
        blueprintObjDir = (self.riggingToolRoot + '/System/Widgets/Layout/')
        print blueprintObjDir
        blueprintFiles = os.listdir(blueprintObjDir)
        for each in blueprintFiles:
            print each