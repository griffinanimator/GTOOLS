""" rotate_order.py """
""" garvey chi - 07-24-11 """
""" module for setting rotation order """


import maya.cmds as cmds

def setRotateOrder(rotationOrder, object):
    
    """Set the Rotation Orders for the selected Node"""
    print object
    for item in range (len(object)):
        cmds.setAttr(object[item] + ".rotateOrder", rotationOrder)