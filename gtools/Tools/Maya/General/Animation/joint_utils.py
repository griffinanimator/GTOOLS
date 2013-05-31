""" Utilities to work with joints """

import maya.cmds as cmds


class Joint_Utils:
    
    def __init__(self):
        print 'init'
        
    def groupJoints(self):

        # Select all the joints.  Change the name of the selection to fit your naming prefix.
        cmds.select('*_jnt*')
        jnts = cmds.ls(sl=True)
        
        for jnt in jnts:
            grpName = (jnt + '_grp')
            cmds.group(jnt, name=grpName)
            cmds.xform(cp=True)
            
            
import maya.cmds as cmds
def groupJoints():
    
    # Select all the joints.  Change the name of the selection to fit your naming prefix.
    cmds.select('*_jnt*')
    jnts = cmds.ls(sl=True)
    
    cmds.select('*ctrl')
    ctrls = cmds.ls(sl=True)
    
    cmds.select('*flcl')
    flcls = cmds.ls(sl=True)
    
    result = 
    
    
    
groupJoints()