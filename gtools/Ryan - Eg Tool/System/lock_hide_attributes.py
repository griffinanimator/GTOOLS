""" lock_hide_attributes.py """
""" garvey chi - 07-24-11 """
""" module for locking attributes """


import maya.cmds as cmds

def lockHideAttr(object, attributes):
    
    """Lock and Hide Attributes for specified object"""
    for items in attributes:
        lock = cmds.setAttr(object + items, lock=True, keyable=False, channelBox=False)
