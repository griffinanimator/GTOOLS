""" FK Controls.py """
""" Author: Ryan Griffin 2011 """
""" Functions for the creation of fk controls """

import maya.cmds as cmds
import csv

class FK_Controls:
    
    def createFKControls(self, joints):
        """ You can define empty lists to store any items that may be created as you run through your for loops """
        """ Any variables defined inside a for loop are throw away because they get overwritten when the loop runs again"""
        
        """ A list outside of the for loop used to store the fk control names.  [] indicates an empty list. """
        fkControls = []
        """ Create another list to store the control groups """
        fkADJGroups = []
        
        """ Iterate through the joints and create a control for each """
        for joint in joints:
            """ Define a name for our control by using the replace command """
            fk_joint = ("FK_" + joint)
            fkJnt = ("FK" + joint)
            controlName = ("CTL_" + fkJnt)
            FKCTL=cmds.circle(name=controlName)
            cmds.setAttr(FKCTL[0] + ".overrideEnabled",1) 
            cmds.setAttr(FKCTL[0] + ".overrideColor",13)
            
            """ Here is where we append the new fk control to the fkControl list """
            fkControls.append(FKCTL)
            print joint
            """ PointConstrain the control to the joint.  We do this so the control is moved to the position of the joint """
            
            tempConstraint = cmds.pointConstraint(fk_joint, FKCTL)
            cmds.rotate (0, 90, 0) 
            """ We no longer need the pointConstraint so we delete it """
            cmds.delete(tempConstraint)
            cmds.makeIdentity(FKCTL[0], apply=True)
            cmds.delete(constructionHistory = True)
            
            """ Now we group the control so we can zero out the controls attributes """
            """ This keeps the control at it's current position while creating clean channels for animation """
            """ Lets make a name for this group """
            ADJGrpName = ('ADJ_' + 'CTL_' + fkJnt) 
            ADJGroup = cmds.group(em=True, name=ADJGrpName)
            
            tempConstraint = cmds.parentConstraint(fk_joint, ADJGroup)
            cmds.delete(tempConstraint)
            
            """ Parent the control to the control group """
            cmds.parent(FKCTL[0], ADJGroup)
            
            """ Append the control group to the fkADJGroup list """
            fkADJGroups.append(ADJGroup)
            
            """ orientConstrain the joint to the control """
            cmds.orientConstraint(FKCTL[0], fk_joint, maintainOffset=True, weight=1)
            cmds.makeIdentity(FKCTL[0], apply=True)
            cmds.delete(constructionHistory = True)
            lockAttr = [ '.translateX', '.translateY', '.translateZ', '.scaleX', '.scaleY', '.scaleZ', '.visibility' ]
            for items in lockAttr:
                lock = cmds.setAttr(FKCTL[0] + items, lock=True, keyable=False, channelBox=False)
                
        """ Now you can do a new for loop for the parenting and orientation """     
        """ joints lives outside the for loop so you can still use it here """        
        """ Now we need to set up a hierarchy that will give us the functionality of an fk arm """
        """ We can do this by parenting each control group to the joint that is one up in the chain.
        Or we can create a hierarchy of control objects.  See the image in the post for details """
        
        for index in range (len(fkControls)):
            if index != 0:
                cmds.parent(fkADJGroups[index], fkControls[index -1][0])
        for index in range (len(fkControls)):
            print fkControls[index][0]
            cmds.setAttr(fkControls[index][0] + ".rotateOrder", 2)
            
        print fkADJGroups    
        for index in range (len(fkADJGroups)):
            print fkADJGroups[index]
            cmds.setAttr(fkADJGroups[index] + ".rotateOrder", 2)
        
        print fkADJGroups[index]
        groupFK = cmds.group(fkADJGroups[0], name='CTL_FKArm_GRP')
        cmds.setAttr(groupFK + ".rotateOrder", 2)