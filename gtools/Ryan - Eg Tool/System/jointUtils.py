""" Joint Utils.py """
""" Author: Ryan Griffin 2011 """
""" Functions for the creation of joints """

import maya.cmds as cmds
import csv

class Joint_Utils:
    def __init__(self):
        """ This is the dictionary """
        self.jointList = {}

    def createJoints(self, jointNames, jointPos):
        """ Check to see if the joint chain exists.  Delete it if it does """
        if cmds.objExists(jointNames[0]):
            cmds.delete(jointNames[0])
        bnJoints=[]
        """ Iterate through the jointNames list and create a joint for each item in the list """
        for index in range (len(jointNames)):
            bnJnt = ("BN_"+jointNames[index])
            bnJoints.append(bnJnt)
            cmds.joint (name=bnJnt, position=jointPos[index])
            cmds.joint (bnJnt, edit=True, zeroScaleOrient=True, orientJoint='xyz', children=True, secondaryAxisOrient='yup')
            
            """Trying to make the joints editable so that I can set their orientation"""
            
            print jointNames[index]
            cmds.setAttr(bnJnt + ".rotateOrder", 2)
            
        """ Deselect the joint """
        cmds.select(d=True)
        """ Here is how you add jointNames to a new key in that dictionary """
        self.jointList['bind'] = jointNames
        return (bnJoints)

    def createFKJoints (self, jointNames, jointPos):
        """ Clearing my selection just in case """
        cmds.select(d=True)
        """ Make an empty list to save new fk joints """
        fkJoints=[]

        for index in range (len(jointNames)):
            fkJnt = ("FK_"+jointNames[index])
            fkJoints.append(fkJnt)
            cmds.joint (name=fkJnt, position=jointPos[index])
            cmds.joint (fkJnt, edit=True, zeroScaleOrient=True, orientJoint='xyz', children=True, secondaryAxisOrient='yup')
            cmds.setAttr(fkJnt + ".rotateOrder", 2)
        self.jointList['fk'] = fkJoints
        return (fkJoints)

    def createIKJoints (self, jointNames, jointPos):
        """ Clearing my selection just in case """
        cmds.select(d=True)
        """ Make an empty list to save new ik joints """
        ikJoints=[]

        for index in range (len(jointNames)):
            ikJnt = ("IK_"+jointNames[index])
            ikJoints.append(ikJnt)
            cmds.joint (name=ikJnt, position=jointPos[index])
            cmds.joint (ikJnt, edit=True, zeroScaleOrient=True, orientJoint='xyz', children=True, secondaryAxisOrient='yup')
            cmds.setAttr(ikJnt + ".rotateOrder", 2)
            #-e -oj xyz -secondaryAxisOrient yup -ch -zso;
        """ Add the ik joints to the dictionary under a 'ik' key """    
        self.jointList['ik'] = ikJoints
        return (ikJoints)

    def newStuff(self):
        """ This function is here to show you the dictionary in action"""
        """ Open the script editor to see the print out """
        joints = self.jointList['bind']
        ikJoints = self.jointList['ik']
        
        print joints
        print ikJoints

    def groupArms (self, jointNames, jointPos):
        """Group the BN Arm, FK Arm, and IK Arm chains together"""
        GrpArm = cmds.group("BN_"+jointNames[0], "FK_"+jointNames[0], "IK_"+jointNames[0], name='JNT_Arm_GRP')
        
