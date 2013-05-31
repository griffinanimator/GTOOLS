""" IK Controls.py """
""" Functions for the creation of joints """

import maya.cmds as cmds
import csv

class Leg_IKFK_Connect:
    
    def leg_connectIKFK(self, joints):
        
        """Create the Leg Control = CTL_Leg"""
        LegCTL = cmds.spaceLocator(name='CTL_Leg')
        print LegCTL
        temp = cmds.pointConstraint('BN_' + joints[3], LegCTL)
        cmds.delete(temp)
        adjLegCTL = cmds.group(empty = True, name=LegCTL[0] + '_ADJ')
        temp = cmds.parentConstraint('BN_' + joints[3], adjLegCTL)
        cmds.delete(temp)
        cmds.parentConstraint('BN_' + joints[3], adjLegCTL, maintainOffset = True)
        cmds.parent(LegCTL[0], adjLegCTL)
        cmds.move( 0, 4, 4, relative = True )
        cmds.setAttr(LegCTL[0] + ".overrideEnabled", 1)
        cmds.setAttr(LegCTL[0] + ".overrideColor", 20)
        cmds.makeIdentity(LegCTL, apply=True)
        cmds.delete(constructionHistory = True)
        scaleAttr = [ '.scaleX', '.scaleY', '.scaleZ' ]
        for x in scaleAttr:
            scaleAttr = cmds.setAttr(LegCTL[0] + x, 0.5)
        
        """Move pivot point of the CTL_Leg"""
        posX = [cmds.getAttr(adjLegCTL + '.translateX')]
        posY = [cmds.getAttr(adjLegCTL + '.translateY')]
        posZ = [cmds.getAttr(adjLegCTL + '.translateZ')]
        wristPos = [posX[0], posY[0], posZ[0]]
        print wristPos
        cmds.move(wristPos[0], wristPos[1], wristPos[2], LegCTL[0] + '.scalePivot', LegCTL[0] + '.rotatePivot')

        lockAttr = [ '.translateX', '.translateY', '.translateZ', '.rotateX', '.rotateY', '.rotateZ', '.scaleX', '.scaleY', '.scaleZ', '.visibility' ]
        for items in lockAttr:
            lock = cmds.setAttr(LegCTL[0] + items, lock=True, keyable=False, channelBox=False)

        """Create Leg IK/FK Switch attribute"""
        cmds.select(LegCTL, replace = True)
        cmds.addAttr(longName = 'Leg_CTLS', attributeType = 'enum', enumName = "--------------------:")
        cmds.setAttr(LegCTL[0] + '.Leg_CTLS', edit = True, keyable = True, lock = True)
        cmds.addAttr(longName = 'IK_FK_Switch', attributeType = 'double', minValue = 0, maxValue = 1, defaultValue = 0)
        cmds.setAttr(LegCTL[0] + '.IK_FK_Switch', keyable = True)
        
        """Connect Attribute of CTL_Leg IK/FK Switch"""
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
            cmds.connectAttr(LegCTL[0] + '.IK_FK_Switch', node + '.blender')
        """
        ""Set Visibility for IK/FK Switch - I'm having trouble passing variables from the ik_controls & fk_controls classes""
        import System.ik_controls as ik_controls
        reload(ik_controls)
        ik_CTLgroups = ik_controls.IK_Controls()
        #ik_CTLgroups.createIKControls()
        cmds.setAttr(LegCTL[0] + '.IK_FK_Switch', 0)
        cmds.setAttr('IK_' + joints[0] + '.visibility', 1)
        cmds.setAttr('CTL_' + IKGrpName[0] + '.visibility', 1)
        cmds.setAttr('FK_' + joints[0] + '.visibility', 0)
        cmds.setAttr('CTL_' + groupFK[0] + '.visibility', 0)
        cmds.setDrivenKeyframe(currentDriver = LegCTL[0] + '.IK_FK_Switch', attribute =  'IK_' + joints[0] +'.visibility')
        cmds.setDrivenKeyframe(currentDriver = LegCTL[0] + '.IK_FK_Switch', attribute =  groupIK[0] +'.visibility')
        cmds.setDrivenKeyframe(currentDriver = LegCTL[0] + '.IK_FK_Switch', attribute =  'FK_' + joints[0] +'.visibility')
        cmds.setDrivenKeyframe(currentDriver = LegCTL[0] + '.IK_FK_Switch', attribute =  groupFK[0] +'.visibility')
        cmds.setAttr(LegCTL[0] + '.IK_FK_Switch', 1)
        cmds.setAttr('FK_' + joints[0] + '.visibility', 1)
        cmds.setAttr('CTL_' + groupFK[0] + '.visibility', 1)
        cmds.setAttr('IK_' + joints[0] + '.visibility', 0)
        cmds.setAttr('CTL_' + groupIK[0] + '.visibility', 0)
        cmds.setDrivenKeyframe(currentDriver = LegCTL[0] + '.IK_FK_Switch', attribute =  'IK_' + joints[0] +'.visibility')
        cmds.setDrivenKeyframe(currentDriver = LegCTL[0] + '.IK_FK_Switch', attribute =  groupIK[0] +'.visibility')
        cmds.setDrivenKeyframe(currentDriver = LegCTL[0] + '.IK_FK_Switch', attribute =  'FK_' + joints[0] +'.visibility')
        cmds.setDrivenKeyframe(currentDriver = LegCTL[0] + '.IK_FK_Switch', attribute =  groupFK[0] +'.visibility')
"""