""" circle_curve.py """
""" garvey chi - 07-26-11 """
""" module for creating NURBS circle curve """


import maya.cmds as cmds

def createNurbsCircle(circleName):

    """create a NURBS curve circle"""
    circle = cmds.circle(name=circleName)