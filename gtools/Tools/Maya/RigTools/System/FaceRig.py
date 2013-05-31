
""" Select the control, the joint, and the folicle """
selList = cmds.ls(sl=True)
print selList

""" make a name for the pma node """
nodeName = selList[0].replace('_ctrl', '_pma_node')
print nodeName

""" Create pma node """
pmaNodeX = cmds.createNode( 'plusMinusAverage', n=nodeName + 'x' )
pmaNodeY = cmds.createNode( 'plusMinusAverage', n=nodeName + 'z' )

""" Define var names for all the objects I need to connect """
control = selList[0]
facJoint = selList[1]
folicle = selList[2]

follicleShape = cmds.listRelatives(folicle, shapes=True)[0]
print follicleShape

""" Parent constraint joint to folicle """
cmds.parentConstraint(folicle, facJoint, mo=True)

""" Connect the control to the pma """
cmds.connectAttr(control + '.tx', pmaNodeX + '.input1D[0]')
cmds.connectAttr(control + '.ty', pmaNodeY + '.input1D[0]')

""" input current folicle UV val to pma node """
follicleUPar = cmds.getAttr(follicleShape + '.parameterU')
cmds.setAttr(pmaNodeX + '.input1D[1]', follicleUPar)

follicleVPar = cmds.getAttr(follicleShape + '.parameterV')
cmds.setAttr(pmaNodeY + '.input1D[1]', follicleVPar)

""" Connect the output of pmaNode to input of folicle """
cmds.connectAttr(pmaNodeX + '.output1D', folicle + '.parameterU')
cmds.connectAttr(pmaNodeY + '.output1D', folicle + '.parameterV')