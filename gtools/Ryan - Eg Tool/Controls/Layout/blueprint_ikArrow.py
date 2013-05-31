""" blueprint_ikArrow.py """
""" garvey chi - 07-13-11 """
""" creates ikArrow blueprint geo """

import maya.cmds as cmds

def blueprintIKArrow():
   
    """ Arrow geo creation """    
    arrow = cmds.polyCube(name = 'blueprint_ikArrow', width = 5, height = 1, subdivisionsX = 2, subdivisionsY = 2, axis = (0, 1, 0))
    cmds.select(arrow)
    cmds.select('blueprint_ikArrow.vtx[1]', 'blueprint_ikArrow.vtx[4]', 'blueprint_ikArrow.vtx[7]', 'blueprint_ikArrow.vtx[10]', 'blueprint_ikArrow.vtx[13]', 'blueprint_ikArrow.vtx[16]')
    cmds.move(2.15, 0, 0, relative=True, objectSpace=True, worldSpaceDistance=True)
    cmds.select('blueprint_ikArrow.f[5]', 'blueprint_ikArrow.f[11]')
    cmds.polyExtrudeFacet(pivotX = 2.325000048)
    cmds.setAttr('polyExtrudeFace1.localTranslate', 0, 0, 0.65, type='double3')
    cmds.select('blueprint_ikArrow.vtx[5]', 'blueprint_ikArrow.vtx[14]')
    cmds.move(1.15, 0, 0, relative=True, objectSpace=True, worldSpaceDistance=True)
    cmds.select('blueprint_ikArrow.vtx[2]', 'blueprint_ikArrow.vtx[8]', 'blueprint_ikArrow.vtx[11]', 'blueprint_ikArrow.vtx[17]')
    cmds.move(0.648, 0, 0, relative=True, objectSpace=True, worldSpaceDistance=True)
    
    """ Create and assign shader """    
    shader = cmds.shadingNode('lambert', name = 'bp_red', asShader=True)
    cmds.select(arrow)
    cmds.hyperShade(assign = shader)
    cmds.setAttr(shader + '.color', 1, 0, 0, type='double3') 
    
    """ Delete history """
    cmds.delete(constructionHistory = True)

blueprintIKArrow()
