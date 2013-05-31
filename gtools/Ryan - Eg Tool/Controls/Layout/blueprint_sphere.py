""" blueprint_sphere.py """
""" garvey chi - 07-12-11 """
""" creates sphere blueprint geo """

import maya.cmds as cmds

def blueprintSphere(name):
    
    """ Create sphere geo """
    sphere = cmds.polySphere (name = name, subdivisionsX = 20, subdivisionsY = 20)
    
    """ Create and assign shader """
    shader = cmds.shadingNode('lambert', name = 'bp_blue', asShader=True)
    cmds.select(sphere)
    cmds.hyperShade(assign = shader)
    cmds.setAttr(shader + '.color', 0, 0.770307, 1, type='double3')
    
    """ Delete History """
    cmds.delete(constructionHistory = True)
    

