""" blueprint_sphere.py """
""" garvey chi - 07-12-11 """
""" creates sphere blueprint geo """

import maya.cmds as cmds
import os

CLASS_NAME = "BPSphere"

TITLE = "BPSphere"
DESCRIPTION = "Creates a sphere "
ICON = os.environ["RIGTOOL"] + "/System/icons/sphere.bmp"


class BPSphere:
    def __init__(self):
        print ' in bpsphere'
 
    def blueprintSphere(self, name):
        
        """ Create sphere geo """
        sphere = cmds.polySphere (name = name, subdivisionsX = 20, subdivisionsY = 20)
        
        """ Create and assign shader """
        shader = cmds.shadingNode('lambert', name = 'bp_blue', asShader=True)
        cmds.select(sphere)
        cmds.hyperShade(assign = shader)
        cmds.setAttr(shader + '.color', 0, 0.770307, 1, type='double3')
        
        """ Delete History """
        cmds.delete(constructionHistory = True)
    
