def createNoFlipKnee(iksSolver, hip, footControl):
    """ Create a locator """

    """ Create a locator to use for the PoleVector"""
    lctrName = "LctrPV_leg"
    lctrPos = cmds.xform(hip, q=True, ws=True, t=True)
    pvPoint = cmds.spaceLocator(n=lctrName, p=lctrPos)
    cmds.xform(cp=True)
    cmds.makeIdentity( apply=True )

    """ Parent the locator to the cog """
    cmds.parent(pvPoint, "jnt_pelvis") #Temp

    """ Constran ikHandle to PV """
    cmds.poleVectorConstraint(pvPoint[0], iksSolver)

    """ Create a twist attribute on the foot control """
    cmds.select(footControl)
    try:
        cmds.addAttr( shortName='twist', longName='twist', defaultValue=0, k=True)
    except:
        print "twist attr may have not been created"
    cmds.select(d=True)

    """ Create an mdiv and a pma node """
    mdivNamePrefix = hip.replace("Jnt_", "mDiv_PV_") 
    mdivNode = cmds.shadingNode("multiplyDivide", asUtility=True, n=mdivNamePrefix)

    pmaNamePrefix = hip.replace("Jnt_", "Pma_PV__") 
    pmaNode = cmds.shadingNode("plusMinusAverage", asUtility=True, n=pmaNamePrefix)

    cmds.connectAttr(footControl+".twist", mdivNode+".input1X")
    cmds.connectAttr(footControl+".ry", mdivNode+".input1Y")
    # Will need to change this with cog
    cmds.connectAttr("jnt_pelvis.ry", mdivNode+".input1Z")

    cmds.setAttr(mdivNode+".input2X", -1)
    cmds.setAttr(mdivNode+".input2Y", -1)
    cmds.setAttr(mdivNode+".input2Z", -1)

    cmds.connectAttr(mdivNode+".input1X", pmaNode+".input1D[0]")
    cmds.connectAttr(mdivNode+".input1Y", pmaNode+".input1D[1]")
    cmds.connectAttr(pmaNode+".output1D", iksSolver+".twist")
    #142.4
    cmds.setAttr(footControl+".twist", 0)
    
    
    
iksSolver = 'ikh_leg'
hip = 'ikj_hip'
footControl = 'ctrl_leg'

createNoFlipKnee(iksSolver, hip, footControl)
