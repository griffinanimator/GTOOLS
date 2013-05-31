""" ik_rp_handle.py """
""" garvey chi - 07-26-11 """
""" module for creating an ik RP handle """


import maya.cmds as cmds

def createIKRPHandle(startJnt, endJnt, solverName, ikHandleName, effectorName):

    """Create an ik handle with RP (rotate plane) solver"""
    ikHandle = cmds.ikHandle(startJoint=startJnt, endEffector=endJnt, solver=solverName, name=ikHandleName)
    cmds.rename(ikHandle[1], effectorName)
    print ikHandle