""" ikfk_connect.py """
""" garvey chi - 05-17-11 """
""" Functions to connect the ik and fk arms """

import maya.cmds as cmds
import csv

class IKFK_Connect:
    
    def connectIKFKArms(self, joints):
        
        """Create the Hand Control = CTL_Hand"""
        handCTL = cmds.spaceLocator(name='CTL_Hand')
        print handCTL
        temp = cmds.pointConstraint('BN_' + joints[2], handCTL)
        cmds.delete(temp)
        adjHandCTL = cmds.group(empty = True, name='ADJ_' + handCTL[0])
        temp = cmds.parentConstraint('BN_' + joints[2], adjHandCTL)
        cmds.delete(temp)
        cmds.parentConstraint('BN_' + joints[2], adjHandCTL, maintainOffset = True)
        cmds.parent(handCTL[0], adjHandCTL)
        cmds.move( 0, 4, 0, relative = True )
        cmds.setAttr(handCTL[0] + ".overrideEnabled", 1)
        cmds.setAttr(handCTL[0] + ".overrideColor", 20)
        cmds.makeIdentity(handCTL, apply=True)
        cmds.delete(constructionHistory = True)
        scaleAttr = [ '.scaleX', '.scaleY', '.scaleZ' ]
        for x in scaleAttr:
            scaleAttr = cmds.setAttr(handCTL[0] + x, 0.5)
        
        """Move pivot point of the CTL_Hand"""
        posX = [cmds.getAttr(adjHandCTL + '.translateX')]
        posY = [cmds.getAttr(adjHandCTL + '.translateY')]
        posZ = [cmds.getAttr(adjHandCTL + '.translateZ')]
        wristPos = [posX[0], posY[0], posZ[0]]
        print wristPos
        cmds.move(wristPos[0], wristPos[1], wristPos[2], handCTL[0] + '.scalePivot', handCTL[0] + '.rotatePivot')

        lockAttr = [ '.translateX', '.translateY', '.translateZ', '.rotateX', '.rotateY', '.rotateZ', '.scaleX', '.scaleY', '.scaleZ', '.visibility' ]
        for items in lockAttr:
            lock = cmds.setAttr(handCTL[0] + items, lock=True, keyable=False, channelBox=False)

        """Create Arm IK/FK Switch attribute"""
        cmds.select(handCTL, replace = True)
        cmds.addAttr(longName = 'ARM_CTLS', attributeType = 'enum', enumName = "--------------------:")
        cmds.setAttr(handCTL[0] + '.ARM_CTLS', edit = True, keyable = True, lock = True)
        cmds.addAttr(longName = 'IK_FK_Switch', attributeType = 'double', minValue = 0, maxValue = 1, defaultValue = 0)
        cmds.setAttr(handCTL[0] + '.IK_FK_Switch', keyable = True)
        
        """Connect Attribute of CTL_Hand IK/FK Switch"""
        blendColorNodes = []
        for joint in joints: 
            
            blendColorTr = cmds.shadingNode('blendColors', asUtility = True, name = 'blendIKFK_tr_' + joint)
            cmds.connectAttr('FK_' + joint + '.translate', blendColorTr + '.color1', force = True)
            cmds.connectAttr('IK_' + joint + '.translate', blendColorTr + '.color2', force = True)
            cmds.connectAttr(blendColorTr + '.output', 'BN_' + joint + '.translate')
            blendColorNodes.append(blendColorTr)
            blendColorRot = cmds.shadingNode('blendColors', asUtility = True, name = 'blendIKFK_rot_' + joint)
            cmds.connectAttr('FK_' + joint + '.rotate', blendColorRot + '.color1', force = True)
            cmds.connectAttr('IK_' + joint + '.rotate', blendColorRot + '.color2', force = True)
            cmds.connectAttr(blendColorRot + '.output', 'BN_' + joint + '.rotate')
            blendColorNodes.append(blendColorRot)
        for node in blendColorNodes:
            cmds.connectAttr(handCTL[0] + '.IK_FK_Switch', node + '.blender')
        """
        ""Set Visibility for IK/FK Switch - I'm having trouble passing variables from the ik_controls & fk_controls classes""
        import System.ik_controls as ik_controls
        reload(ik_controls)
        ik_CTLgroups = ik_controls.IK_Controls()
        #ik_CTLgroups.createIKControls()
        cmds.setAttr(handCTL[0] + '.IK_FK_Switch', 0)
        cmds.setAttr('IK_' + joints[0] + '.visibility', 1)
        cmds.setAttr('CTL_' + IKGrpName[0] + '.visibility', 1)
        cmds.setAttr('FK_' + joints[0] + '.visibility', 0)
        cmds.setAttr('CTL_' + groupFK[0] + '.visibility', 0)
        cmds.setDrivenKeyframe(currentDriver = handCTL[0] + '.IK_FK_Switch', attribute =  'IK_' + joints[0] +'.visibility')
        cmds.setDrivenKeyframe(currentDriver = handCTL[0] + '.IK_FK_Switch', attribute =  groupIK[0] +'.visibility')
        cmds.setDrivenKeyframe(currentDriver = handCTL[0] + '.IK_FK_Switch', attribute =  'FK_' + joints[0] +'.visibility')
        cmds.setDrivenKeyframe(currentDriver = handCTL[0] + '.IK_FK_Switch', attribute =  groupFK[0] +'.visibility')
        cmds.setAttr(handCTL[0] + '.IK_FK_Switch', 1)
        cmds.setAttr('FK_' + joints[0] + '.visibility', 1)
        cmds.setAttr('CTL_' + groupFK[0] + '.visibility', 1)
        cmds.setAttr('IK_' + joints[0] + '.visibility', 0)
        cmds.setAttr('CTL_' + groupIK[0] + '.visibility', 0)
        cmds.setDrivenKeyframe(currentDriver = handCTL[0] + '.IK_FK_Switch', attribute =  'IK_' + joints[0] +'.visibility')
        cmds.setDrivenKeyframe(currentDriver = handCTL[0] + '.IK_FK_Switch', attribute =  groupIK[0] +'.visibility')
        cmds.setDrivenKeyframe(currentDriver = handCTL[0] + '.IK_FK_Switch', attribute =  'FK_' + joints[0] +'.visibility')
        cmds.setDrivenKeyframe(currentDriver = handCTL[0] + '.IK_FK_Switch', attribute =  groupFK[0] +'.visibility')
"""