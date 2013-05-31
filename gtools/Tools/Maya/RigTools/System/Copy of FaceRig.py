""" Select the control, the joint, and the folicle """
selList = cmds.ls(sl=True)
print selList

""" make a name for the pma node """
nodeName = selList[0].replace('_ctrl', '_pma_node')
mdivName = selList[0].replace('_ctrl', '_md_node')
print nodeName
print mdivName

""" Create pma node """
pmaNodeX = cmds.createNode( 'plusMinusAverage', n=nodeName + 'x' )
pmaNodeY = cmds.createNode( 'plusMinusAverage', n=nodeName + 'z' )

""" an mdiv node to offset scale """
mdivNode = cmds.createNode( 'multiplyDivide', n=mdivName) 
""" Set attrs """
cmds.setAttr (mdivNode + '.operation', 1)
cmds.setAttr (mdivNode + '.input2X', 1)
cmds.setAttr (mdivNode + '.input2Y', 1)

""" Define var names for all the objects I need to connect """
control = selList[0]
folicle = selList[1]

follicleShape = cmds.listRelatives(folicle, shapes=True)[0]


""" Connect the control to the mdiv and the mdiv to the pma """
cmds.connectAttr(control + '.tx', mdivNode + '.input1X')
cmds.connectAttr(control + '.ty', mdivNode + '.input1Y')

cmds.connectAttr(mdivNode + '.outputX', pmaNodeX + '.input1D[0]')
cmds.connectAttr(mdivNode + '.outputY', pmaNodeY + '.input1D[0]')

""" input current folicle UV val to pma node """
follicleUPar = cmds.getAttr(follicleShape + '.parameterU')
cmds.setAttr(pmaNodeX + '.input1D[1]', follicleUPar)

follicleVPar = cmds.getAttr(follicleShape + '.parameterV')
cmds.setAttr(pmaNodeY + '.input1D[1]', follicleVPar)

""" Connect the output of pmaNode to input of folicle """
cmds.connectAttr(pmaNodeX + '.output1D', folicle + '.parameterU')
cmds.connectAttr(pmaNodeY + '.output1D', folicle + '.parameterV')

""" Create a space locator at each control """
lctrPos = cmds.xform(control, q=True, os=True, t=True)

lctrName = selList[0].replace('_ctrl', '_lctr')
lctr = cmds.spaceLocator(n=lctrName, p=lctrPos)
cmds.xform(lctr, ws=True, p=True)
cmds.xform(lctr, cp=True)