""" blueprint_tube.py """
""" garvey chi - 07-13-11 """
""" creates tube blueprint geo """

import maya.cmds as cmds

def blueprintTube(name):
    
    """ Create tube geo """
    tube = cmds.polyCylinder (name = name, subdivisionsX = 20, radius = 0.5, height = 6, axis = (1, 0, 0))
    
    """ Create and assign shader """
    shader = cmds.shadingNode('lambert', name = 'bp_orange', asShader=True)
    cmds.select(tube)
    cmds.hyperShade(assign = shader)
    cmds.setAttr(shader + '.color', 1, 00.58725, 0.27, type='double3') 
    
    """ Delete history """
    cmds.delete(constructionHistory = True)
    