import maya.cmds as cmds

footCtrl = cmds.ls(sl=True)
cmds.addAttr( shortName='Toe_Roll', longName='Toe_Roll', defaultValue=0,  k=True)
cmds.addAttr( shortName='Toe_Twist', longName='Toe_Twist', defaultValue=0,  k=True)
cmds.addAttr( shortName='Ball_Roll', longName='Ball_Roll', defaultValue=0,  k=True)
cmds.addAttr( shortName='Ball_Twist', longName='Ball_Twist', defaultValue=0,  k=True)
cmds.addAttr( shortName='Ball_Bank', longName='Ball_Bank', defaultValue=0,  k=True)
cmds.addAttr( shortName='Heel_Roll', longName='Heel_Roll', defaultValue=0,  k=True)
cmds.addAttr( shortName='Heel_Twist', longName='Heel_Twist', defaultValue=0,  k=True)


cmds.connectAttr('ctrl_leg.Toe_Roll', 'grp_toe.rx')
 
cmds.connectAttr('ctrl_leg.Toe_Twist', 'grp_toe.ry')
 
cmds.connectAttr('ctrl_leg.Ball_Roll', 'grp_ball.rx')
 
cmds.connectAttr('ctrl_leg.Ball_Twist', 'grp_ball.ry')
 
cmds.connectAttr('ctrl_leg.Ball_Bank', 'grp_ball.rz')
 
cmds.connectAttr('ctrl_leg.Heel_Roll', 'grp_heel.rx')
 
cmds.connectAttr('ctrl_leg.Heel_Twist', 'grp_heel.ry')

kneeTx = cmds.getAttr('ikj_knee.tx')
print kneeTx
ankleTx = cmds.getAttr('ikj_ankle.tx')
print ankleTx

legLen =  (kneeTx + ankleTx)
print legLen


6.24220144151
8.03225328932
14.2744547308

