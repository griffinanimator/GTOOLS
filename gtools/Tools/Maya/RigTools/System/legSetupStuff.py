"""Instructions for foot roll """
""" Get the position of the ball and toe joints """
ballJoint_modulePos = cmds.xform('ikj_ball', ws=True, t=True, q=True)

""" Create 3 locators to be used for roll attribute """
rollLctrs = []
dynRollLctr = cmds.spaceLocator(name='dynRoll_lctr')[0]
cmds.xform(dynRollLctr, a=True, t=ballJoint_modulePos)
rollLctrs.append(dynRollLctr)


statRollLctr = cmds.spaceLocator(name='statRoll_lctr')[0]
cmds.xform(statRollLctr, a=True, t=ballJoint_modulePos)
rollLctrs.append(statRollLctr)


""" heelRoll_lctr """
heelRollLctr = cmds.spaceLocator(name='heelRoll_lctr')[0]
cmds.xform(heelRollLctr, a=True, t=ballJoint_modulePos)
rollLctrs.append(heelRollLctr)



""" Parent the locators to the ik grps """
cmds.parent(dynRollLctr, 'ctrl_leg')
cmds.parent(heelRollLctr, 'ctrl_leg')
cmds.parent(statRollLctr, 'grp_heel')

""" Parent constrain ball and toe groups to roll_lctrs """
parentConstraints = []
rollParentConstraint = cmds.parentConstraint(dynRollLctr, 'grp_ball', mo=True, st=('x', 'y', 'z'), sr=('y', 'z'))
parentConstraints.append(rollParentConstraint[0])
rollParentConstraint = cmds.parentConstraint(statRollLctr, 'grp_ball', mo=True, st=('x', 'y', 'z'), sr=('y', 'z'))
parentConstraints.append(rollParentConstraint[0])
rollParentConstraint = cmds.parentConstraint(statRollLctr, 'grp_toe', mo=True, st=('x', 'y', 'z'), sr=('y', 'z'))
parentConstraints.append(rollParentConstraint[0])
rollParentConstraint = cmds.parentConstraint(dynRollLctr, 'grp_toe', mo=True, st=('x', 'y', 'z'), sr=('y', 'z'))
parentConstraints.append(rollParentConstraint[0])



""" Create a remap value node to control foot roll """
cmds.createNode('remapValue', name ='roll_rv')


""" Create a remap value node to control foot roll """
cmds.createNode('remapValue', name ='roll_rv')
cmds.setAttr('roll_rv.inputMax', 180.0)
""" Connect to the remap value node """
"""" Connect the output of dynRollLctr to roll_rv input value """
cmds.connectAttr(dynRollLctr + '.rx', 'roll_rv.inputValue' )
""" roll_break to input min """
cmds.setAttr('ctrl_leg.Roll_Break', 45.0)
cmds.connectAttr('ctrl_leg.Roll_Break', 'roll_rv.inputMin')
""" roll_break to parent constraint switches """
cmds.connectAttr('roll_rv.outColorG', 'grp_ball' + '.blendParent2')
cmds.connectAttr('roll_rv.outColorR', 'grp_toe' + '.blendParent2')


""" constrain the heelRoll_grp to heelRoll_lctr.  Switch off the constraint when greater than 0 """
cmds.createNode('condition', name='roll_cond')
heelOrientConstraint = cmds.orientConstraint(heelRollLctr, 'grp_heel', skip=('y', 'z'), mo=True)
heelOrientAttr = (heelOrientConstraint[0] + '.' + heelRollLctr +'W0')
cmds.connectAttr('roll_cond.outColorR', heelOrientAttr)
cmds.connectAttr(heelRollLctr + '.rx', 'roll_cond.firstTerm')
cmds.setAttr('roll_cond.operation', 3)
