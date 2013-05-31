""" leg_ik_controls.py """
""" garvey chi - 05-17-11 """
""" Functions for the creation of an ik leg """

import maya.cmds as cmds
import csv

class Leg_IK_Controls:
    
    def leg_createIKControls(self, joints):
        
        ikHandle = cmds.ikHandle(startJoint='IK_'+joints[0], endEffector='IK_'+joints[2], solver='ikRPsolver', name='ikHandle_leg')
        cmds.rename(ikHandle[1], 'effectorleg')
        print ikHandle
        
        """Create IK leg Control"""
        legIKCTL = cmds.circle(name='CTL_IKleg')
        print legIKCTL
        cmds.setAttr(legIKCTL[0] + ".overrideEnabled",1)
        cmds.setAttr(legIKCTL[0] + ".overrideColor",12)
        temp = cmds.pointConstraint("IK_" + joints[2], legIKCTL[0])
        cmds.delete(temp)
        
        scaleAttr = [ '.scaleX', '.scaleY', '.scaleZ' ]
        for x in scaleAttr:
            scaleAttr = cmds.setAttr(legIKCTL[0] + x, 1.5)
        cmds.setAttr(legIKCTL[0] + '.rx', 90)
        IKGrpName = (legIKCTL[0] + '_GRP') 
        adjIKCTL = cmds.group(empty = True, name=legIKCTL[0] + '_ADJ')
        temp = cmds.parentConstraint("IK_" + joints[2], adjIKCTL)
        cmds.delete(temp)
        cmds.parent(legIKCTL[0], adjIKCTL)
        cmds.makeIdentity(legIKCTL, apply=True)
        cmds.delete(constructionHistory = True)
        
        "Create CTL_IKLeg Group"
        groupIK  = cmds.group(empty = True, name = legIKCTL[0] + '_GRP')
        temp = cmds.pointConstraint(legIKCTL[0], groupIK)
        cmds.delete(temp)
        
        """Parent the ikHandle_Leg under adj node and under the CTL_IKLeg Group"""
        adjIKHandle = cmds.group(empty = True, name = ikHandle[0] + '_ADJ')
        temp = cmds.pointConstraint(legIKCTL[0], adjIKHandle)
        cmds.delete(temp)
        cmds.parent(ikHandle[0], adjIKHandle)
        cmds.parent(adjIKHandle, legIKCTL[0])
        cmds.parent(adjIKCTL, groupIK)
        
        
        """Lock Attributes for the legIKCTL"""
        lockAttr = [ '.scaleX', '.scaleY', '.scaleZ', '.visibility' ]
        for items in lockAttr:
            lock = cmds.setAttr(legIKCTL[0] + items, lock=True, keyable=False, channelBox=False)
        
        """Create IK Leg pole vector constraint"""
        locator1 = cmds.spaceLocator(name='CTL_' + joints[1] + 'Aim')
        print locator1
        temp = cmds.pointConstraint("IK_" + joints[1], locator1[0])
        cmds.delete(temp)
        cmds.move(20, z = True)
        cmds.setAttr(locator1[0] + ".overrideEnabled",1)
        cmds.setAttr(locator1[0] + ".overrideColor",13)
        elbowPoleVector = cmds.poleVectorConstraint(locator1[0], ikHandle[0], weight=1)
        elbAdjNode = cmds.group(empty = True, name = locator1[0] + '_ADJ')
        temp = cmds.pointConstraint(locator1, elbAdjNode)
        cmds.delete(temp)
        cmds.parent(locator1[0], elbAdjNode)
        cmds.parent(elbAdjNode, groupIK)
        
        """Lock Attributes for the CTL_elbowAim"""
        lockAttr = [ '.rotateX', '.rotateY', '.rotateZ', '.scaleX', '.scaleY', '.scaleZ', '.visibility' ]
        for items in lockAttr:
            lock = cmds.setAttr(locator1[0] + items, lock=True, keyable=False, channelBox=False)
        
        legCTLVariables = [ikHandle[0], legIKCTL[0], IKGrpName, adjIKCTL, groupIK, adjIKHandle]
        print legCTLVariables
        for index in range (len(legCTLVariables)):
            cmds.setAttr(legCTLVariables[index] + ".rotateOrder", 1)