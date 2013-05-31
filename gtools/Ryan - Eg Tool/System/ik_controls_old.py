""" IK Controls.py - version 2.0"""
""" garvey chi - 07-21-11 """
""" Functions for the creation of joints """

import maya.cmds as cmds
import csv

class IK_Controls:
    
    def __init__(self):
        
        self.moduleInfo = []
    
    def createIKControls(self, joints, limb, side):
        
        ikHandle = cmds.ikHandle(startJoint='IK_'+joints[0], endEffector='IK_'+joints[2], solver='ikRPsolver', name='ikHandle_Arm')
        cmds.rename(ikHandle[1], 'effectorArm')
        print ikHandle
        """Create IK Control"""
        IKCTL = cmds.circle(name='CTL_IK' + limb + side)
        print IKCTL
        cmds.setAttr(IKCTL[0] + ".overrideEnabled",1)
        cmds.setAttr(IKCTL[0] + ".overrideColor",12)
        temp = cmds.pointConstraint("IK_" + joints[2], IKCTL[0])
        cmds.delete(temp)
        scaleAttr = [ '.scaleX', '.scaleY', '.scaleZ' ]
        for x in scaleAttr:
            scaleAttr = cmds.setAttr(IKCTL[0] + x, 1.5)
        cmds.setAttr(IKCTL[0] + '.ry', 90)
        IKGrpName = (IKCTL[0] + '_GRP') 

    """Create ADJ group for CTL_IK'limb' """
        import.System.adj_node
        reload(adj_node)
        adj_node.createAdjNode("IK_" + joints[2], IKCTL[0] + '_ADJ')


        cmds.parent(IKCTL[0], IKCTL[0] + '_ADJ')
        cmds.makeIdentity(IKCTL, apply=True)
        cmds.delete(constructionHistory = True)


    """Create CTL_IK'limb' group"""
        import.System.adj_node
        reload(adj_node)
        adj_node.createAdjNode(IKCTL[0], 'CTL_IK' + limb + '_GRP')

    """Create ADJ node for ikHandle_'limb' """
        import.System.adj_node
        reload(adj_node)
        adj_node.createAdjNode(IKCTL[0], ikHandle[0] + '_ADJ')

        """Parent the ikHandle_"Limb" under ADJ node and under the CTL_IK"Limb" Group"""
        cmds.parent(ikHandle[0], ikHandle[0] + '_ADJ')
        cmds.parent(ikHandle[0] + '_ADJ', IKCTL[0])
        cmds.parent(adjIKCTL, group)

    """Lock Attributes for the IKCTL"""
        import.System.lock_hide_attributes
        reload(lock_hide_attributes)
        lock_hide_attributes.lockHideAttr(IKCTL[0], ('.scaleX', '.scaleY', '.scaleZ', '.visibility'))


    """Create a Pole Vector Control"""
        import.System.pole_vector
        reload(pole_vector)
        pole_vector.createPoleVector('CTL_' + joints[1] + 'Aim', ikHandle[0])


    """Lock Attributes for the Pole Vector Control"""
        import.System.pole_vector
        reload(pole_vector)
        poleVectorCtl = 'CTL_' + joints[1] + 'Aim'
        pole_vector.createPoleVector(hingeJnt, ikHandle[0], poleVectorCtl,  poleVectorCtl + '_ADJ'):


        cmds.parent(poleVectorCtl[0], poleVectorCtl + '_ADJ')
        cmds.parent(poleVectorCtl + '_ADJ', 'CTL_IK' + limb + '_GRP')


    """Set the Rotation Order of controls and group nodes"""
        import.System.rotate_order
        reload(rotate_order)
        rotate_order.setRotateOrder(2, ikHandle[0], IKCTL[0], 'CTL_IK' + limb + '_GRP', IKCTL[0] + '_ADJ', 'CTL_IK' + limb + '_GRP', ikHandle[0] + '_ADJ')
