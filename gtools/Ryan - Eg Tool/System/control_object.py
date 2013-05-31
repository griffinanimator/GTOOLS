""" control_object.py """
""" garvey chi - 07-26-11 """
""" module for creating and determining the control object """


import maya.cmds as cmds

def createControlObj(ctlName, destTarget):
    
    def createNurbsCircle(self):
    """create a control object"""
    import System.circle_curve
    reload(circle_curve)
    circle_curve.createNurbsCircle(circleName):
    
    """create a control object"""
    IKCTL = cmds.circle(name=ctlName)
    print IKCTL
    cmds.setAttr(IKCTL[0] + ".overrideEnabled",1)
    cmds.setAttr(IKCTL[0] + ".overrideColor",12)
    temp = cmds.pointConstraint(destTarget, IKCTL[0])
    cmds.delete(temp)
    