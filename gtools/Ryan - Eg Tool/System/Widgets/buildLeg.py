""" buildLeg.py """
""" A module for building a leg """    

import maya.cmds as cmds
import os
import sys    
    
class Build_Leg:
    print "Build Leg"  
    
    def buildLeg(self, *args):
        """ This is where we instance in the csvUtils class """
        import System.leg_csv_utils as leg_csv_Utils
        reload (leg_csv_Utils)
        csvRead = leg_csv_Utils.leg_csvRead()        
        
        """ Use the readCsv function to get joint names and positions """
        """ csvRead returns the names and positions.  We save this info into a local variable called jointData """
        jointData = csvRead
        
        """ Now we can replace our old hard coded values with dynamic data pulled from the csv """
        joints = jointData[0]
        positions = jointData[1]
        
        """ Call the create joints function, passing in our joint names and positions """
        """ First instance in the jointUtils """
        import System.leg_jointUtils as leg_jointUtils
        reload (leg_jointUtils)
        jointCreate = leg_jointUtils.Leg_Joint_Utils()
        jointCreate.leg_createJoints (joints, positions)
        
        jointCreate.leg_createFKJoints (joints, positions)
        jointCreate.leg_createIKJoints (joints, positions)
        #jointCreate.grouplegs (joints, positions)
        
        """ Create the fk controls """
        """ Finally we instance in the FK_Controls class """
        import System.leg_fk_controls as leg_fk_controls
        reload(leg_fk_controls)
        fkCreate = leg_fk_controls.Leg_FK_Controls()
        fkCreate.leg_createFKControls(joints)
        
        """Create the IK controls and IK Handle"""
        import System.leg_ik_controls as leg_ik_controls
        reload(leg_ik_controls)
        ikCreate = leg_ik_controls.Leg_IK_Controls()
        ikCreate.leg_createIKControls(joints)
        
        """Create the legCTL, then connect IKFK Legs"""
        import System.leg_ikfk_connect as leg_ikfk_connect
        reload (leg_ikfk_connect)
        legConnect = leg_ikfk_connect.Leg_IKFK_Connect()
        legConnect.leg_connectIKFK(joints)