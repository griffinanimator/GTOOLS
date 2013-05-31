""" adj_node.py """
""" garvey chi - 07-24-11 """
""" module for creating an adjustment node """


import maya.cmds as cmds

def createAdjNode(master, adjNodeName):
        
    """Create Group (Adjustment) Node at the specified location"""
    group  = cmds.group(empty = True, name = adjNodeName)
    temp = cmds.pointConstraint(master, adjNodeName)
    cmds.delete(temp)
    
    return group
