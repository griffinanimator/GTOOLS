""" IK Controls.py - version 2.0"""
""" garvey chi - 07-21-11 """
""" Functions for the creation of joints """

import maya.cmds as cmds
import csv
import System.adj_node as adj_node
reload(adj_node)
import System.lock_hide_attributes as lock_hide_attr
reload(lock_hide_attr)
import pole_vector as pole_vector
reload(pole_vector)
import System.rotate_order as rotate_order
reload(rotate_order)
import System.ik_rp_handle as ik_rp_handle
reload (ik_rp_handle)
#import Controls.Layout.blueprint_sphere as blueprint_sphere
#reload (blueprint_sphere)
        
class IK_Controls:
    
    def __init__(self):
        print 'init'
        self.moduleInfo = []

    def createAdjNode(self): 
        """Create ADJ group"""
        adj_node.createAdjNode(master, adjNodeName)

    def lockHideAttr(self):
        """Lock Attributes"""
        lock_hide_attr.lockHideAttr(object, attributes)

    def pole_vector(self):
        """Create a Pole Vector Control"""
        pole_vector.createPoleVector(hingeJnt, ik_handle, poleVectorCtl, AdjNodeName)

    def rotate_order(self):
        """Set the Rotation Orders for the selected Node"""
        rotate_order.setRotateOrder(rotationOrder, object)

    def createIKRPHandle(self):
        """Create an ik RP handle"""
        ik_rp_handle.createIKRPHandle(startJnt, endJnt, solverName, ikHandleName, effectorName)

    def createControlObj(self):
        """create a control object"""
        control_object.createControlObj(ctlName, destTarget)

    def createIKRPHandle(self):
        """create an ik rp handle"""
        ik_rp_handle.createIKRPHandle(startJnt, endJnt, solverName, ikHandleName, effectorName)

    def createIKControls(self, joints, limb, side):
        """Create IK RP Handle"""
        ikHandle = ik_rp_handle.createIKRPHandle('IK_' + joints[0], 'IK_' + joints[2], 'ikRPsolver', 'ikHandle' + limb, limb + 'Effector')
        ikHandleName = 'ikHandle' + limb
        print ikHandleName
        
        """Create IK Control"""
        IKCTL = cmds.circle(name='CTL_IK' + limb + side)
        #The circle creation code above can be substituted with blueprint geo or another type of 'ctl' object 
        #ie. IKCTL = blueprint_sphere.blueprintSphere('CTL_IK' + limb + side)
        print IKCTL
        cmds.setAttr(IKCTL[0] + ".overrideEnabled",1)
        cmds.setAttr(IKCTL[0] + ".overrideColor",12)
        temp = cmds.pointConstraint("IK_" + joints[2], IKCTL[0])
        cmds.delete(temp)
        scaleAttr = [ '.scaleX', '.scaleY', '.scaleZ' ]
        for x in scaleAttr:
            scaleAttr = cmds.setAttr(IKCTL[0] + x, 1.5)
        cmds.setAttr(IKCTL[0] + '.ry', 90)
        IKCtlGrp = (IKCTL[0] + '_GRP')
        
        """Create ADJ group for CTL_IK'limb' """
        adjIkCtl = adj_node.createAdjNode(IKCTL[0],'ADJ_' + IKCTL[0])
        print adjIkCtl

        """Parent the IK_CTL under its ADJ node, then delete IK_CTL's history"""
        cmds.parent(IKCTL[0], adjIkCtl)
        cmds.makeIdentity(IKCTL, apply=True)
        cmds.delete(constructionHistory = True)

        """Create CTL_IK'limb' group"""
        ikGrpName = adj_node.createAdjNode(IKCTL[0], 'CTL_IK' + limb + '_GRP')
        print ikGrpName

        """Create ADJ node for ikHandle_'limb' """
        adjIkHandle = adj_node.createAdjNode(IKCTL[0], 'ADJ_' + ikHandleName)

        """Parent the ikHandle under ADJ node, then parent ikHandle to the IK_CTL curve. Finally, parent the 
        IK Control ADJ node under the CTL_IK "Limb" Group"""
        cmds.parent(ikHandleName, adjIkHandle)
        cmds.parent(adjIkHandle, IKCTL[0])
        cmds.parent(adjIkCtl, ikGrpName)

        """Lock Attributes for the IKCTL"""
        lock_hide_attr.lockHideAttr(IKCTL[0], ('.scaleX', '.scaleY', '.scaleZ', '.visibility'))

        """Create a Pole Vector Control"""
        poleVectorCtl = 'CTL_' + joints[1] + 'Aim'
        pole_vector.createPoleVector("IK_" + joints[1], ikHandleName, poleVectorCtl, 'ADJ_' + poleVectorCtl)
        adjPoleVectorCtl = 'ADJ_' + poleVectorCtl
        print poleVectorCtl
        print adjPoleVectorCtl

        """Lock Attributes for the Pole Vector Control"""
        lock_hide_attr.lockHideAttr(poleVectorCtl, ('.rotateX', '.rotateY', '.rotateZ', '.scaleX', '.scaleY', '.scaleZ', '.visibility'))

        """Parent the Pole Vector Control to ADJ node, then parent the ADJ node to the CTL_IK "Limb" Group"""
        cmds.parent(poleVectorCtl, adjPoleVectorCtl)
        cmds.parent(adjPoleVectorCtl, ikGrpName)

        """Set the Rotation Order of controls and group nodes"""
        rotate_order.setRotateOrder(2, (ikHandleName, IKCTL[0], ikGrpName, adjIkCtl, adjIkHandle))
