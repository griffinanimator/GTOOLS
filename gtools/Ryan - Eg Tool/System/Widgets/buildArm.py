""" build_arm.py """
""" Author: Ryan Griffin 2011 """
""" A module for building an arm """    

import maya.cmds as cmds
import os
import sys    

CLASS_NAME = "Build_Arm"

TITLE = "Build_Arm"
DESCRIPTION = "Creates an arm set-up "
ICON = os.environ["RIGTOOL"] + "/System/icons/arm.bmp"

class Build_Arm:
    print "Build Arm"  
    
    def buildArm(self, *args):
        """ This is where we instance in the csvUtils class """
        import System.csv_utils as csvUtils
        reload (csvUtils)
        csvRead = csvUtils.csvRead()        
        
        """ Use the readCsv function to get joint names and positions """
        """ csvRead returns the names and positions.  We save this info into a local variable called jointData """
        jointData = csvRead
        
        """ Now we can replace our old hard coded values with dynamic data pulled from the csv """
        joints = jointData[0]
        positions = jointData[1]
        
        
        """ Call the create joints function, passing in our joint names and positions """
        """ First instance in the jointUtils """
        import System.jointUtils as jointUtils
        reload (jointUtils)
        jointCreate = jointUtils.Joint_Utils()
        jointCreate.createJoints (joints, positions)
        
        jointCreate.createFKJoints (joints, positions)
        jointCreate.createIKJoints (joints, positions)
        #jointCreate.groupArms (joints, positions)
        
        """ Create the fk controls """
        """ Finally we instance in the FK_Controls class """
        import System.fk_controls as fk_controls
        reload(fk_controls)
        fkCreate = fk_controls.FK_Controls()
        fkCreate.createFKControls(joints)
        
        """Create the IK controls and IK Handle"""
        import System.ik_controls as ik_controls
        import System.ik_rp_handle as ik_rp_handle
        reload(ik_controls)
        reload(ik_rp_handle)
        ikCreate = ik_controls.IK_Controls()
        ikCreate.createIKControls(joints, 'Arm', '_L')
        
        
        """Create the handCTL, then connect IKFK Arms"""
        import System.ikfk_connect as ikfk_connect
        reload (ikfk_connect)
        armConnect = ikfk_connect.IKFK_Connect()
        armConnect.connectIKFKArms(joints)