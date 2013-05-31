""" pole_vector.py """
""" garvey chi - 07-24-11 """
""" module for creating a pole vector setup"""


import maya.cmds as cmds
import System.adj_node as adj_node
reload(adj_node) 

def createPoleVector(hingeJnt, ikHandleName, poleVectorCtl, adjNodeName):
    
    """Create IK pole vector constraint"""
    locator = cmds.spaceLocator(name = poleVectorCtl)
    print locator
    temp = cmds.pointConstraint(hingeJnt, poleVectorCtl)
    cmds.delete(temp)
    cmds.move(-20, z = True)
    cmds.setAttr(poleVectorCtl + ".overrideEnabled", 1)
    cmds.setAttr(poleVectorCtl + ".overrideColor", 13)
    poleVector = cmds.poleVectorConstraint(poleVectorCtl, ikHandleName, weight=1)

    """Create poleVector ADJ node"""
    adjNode = adj_node.createAdjNode(poleVectorCtl, adjNodeName)