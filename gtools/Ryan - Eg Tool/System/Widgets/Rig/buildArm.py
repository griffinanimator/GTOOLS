""" build_arm.py """
""" A module for building an arm """    

import maya.cmds as cmds
import os
import sys   

""" This is where we instance in the csvUtils class """
import System.csv_utils as csvUtils
reload (csvUtils) 

import System.jointUtils as jointUtils
reload (jointUtils)

import System.fk_controls as fk_controls
reload(fk_controls) 

import System.ik_controls as ik_controls
reload(ik_controls)  

 
class Build_Arm:
    def __init__(self):
        self.jointNames = {}
        
        """ I am storing all the names for the joint chains into dictionaries """
        self.jointNames['bindJnts'] = ("arm_1_bind_joint", "arm_2_bind_joint", "arm_3_bind_joint" ) 
        self.jointNames['fkJnts'] = ("arm_1_fk_joint", "arm_2_fk_joint", "arm_3_fk_joint" )
        self.jointNames['ikJnts'] = ("arm_1_ik_joint", "arm_2_ik_joint", "arm_3_ik_joint" )  
        
        riggingToolRoot = os.environ["RIGTOOL"]
        self.path = "R:/System/CSV_files/armCsv.csv"
        """ Specify a control object to use """
        self.control = (self.path + "controlA.ma")
      
    def buildArm(self, *args):
        """ Use the number of items in self.jointNames to determine number of joint chains to build. """
        """ With this we can get rid of buildFK and IK joints """
        numChains = len(self.jointNames)
           
        jointPos = []        
        
        """ lets try getting our joint names and positions from the locators """
        #jointLctrs = cmds.ls(sl=True)
        #cmds.select(d=True)
        #for lctr in jointLctrs:
            #pos = cmds.getAttr(lctr + ".localPosition")
            #jointPos.append(pos)
        #cmds.delete(jointLctrs)
        
        
        bindJoints = self.jointNames['bindJnts'] 
        fkJoints = self.jointNames['fkJnts']
        ikJoints = self.jointNames['ikJnts']
        
        positions = jointPos
        
        
        """ Call the create joints function, passing in our joint names and positions """
        """ First instance in the jointUtils """
        jointCreate = jointUtils.Joint_Utils()
        
        for index in range(len(self.jointNames)):
            if index == 0:
                joints = self.jointNames['bindJnts']
            if index == 1:
                joints = self.jointNames['fkJnts']
            if index == 2:
                joints = self.jointNames['ikJnts']
  
            jointCreate.createJoints (joints, positions)
            jointCreate.orientJoints(joints)
        
        """ We can use the dictionaries to pass the joint names """    
        jointCreate.groupJoints(bindJoints, fkJoints, ikJoints)
        
        jointCreate.connectJoints(bindJoints, fkJoints, ikJoints)
     
        
        """ Create the fk controls """
        """ instance in the FK_Controls class """
        control = self.control
        fkCreate = fk_controls.FK_Controls()
        fkCreate.createFKControls(fkJoints, control)
        
        """ Create the IK Setup """
        """ Garvey did some nice work with this """
        ikCreate = ik_controls.IK_Controls()
        ikCreate.createIKControls(ikJoints)
        
        
        """ Try writing the saveCsv stuff back into here.  This way you will have a backup"""
        """ of all the info you need to re-create your rig. """
        
        fileName = "arm.csv"
        csvUtils.csvWrite(bindJoints, positions, fileName)
        
        
        
