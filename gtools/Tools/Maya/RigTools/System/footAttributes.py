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

cmds.connectAttr('ctrl_leg.Toe_Flap', 'grp_flap.rx')

cmds.addAttr( shortName='Toe_Flap', longName='Toe_Flap', defaultValue=0, minValue=0, maxValue=1, k=True)

