""" blueprint_UI.py """
""" garvey chi - 07-13-11 """
""" UI containing blueprint tools and utilities """

import maya.cmds as cmds

import os

fileDirectory = (riggingToolRoot + R:\System\Widgets\Layout)

allFiles = os.listdir(fileDirectory) 

print allFiles 

CLASS NAME = "Jaw"
TITLE = "Jaw"

DESCRIPTION = 'Does stuff' 

ICON = '1.bmp'

class Hinge():
    
    def __init__(self):
    
        jointInfo = [["1_joint", [0.0, 0.0, 0.0]], ["2_joint", [0.0, 4.0, 0.0]]]
        #Call on the blueprints initialization 
        blueprintMod.Blueprint.__init__(self, CLASS_NAME, userSpecifiedName, jointInfo)