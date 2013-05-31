""" buildHinge.py """
""" garvey chi - 07-16-11 """
""" module for creating hinge blueprint geo """

import maya.cmds as cmds
import os
import sys    
import System.utils as utils
reload(utils)
import Controls.Layout.blueprint_sphere as blueprint_sphere  
reload(blueprint_sphere)
import Controls.Layout.blueprint_tube as blueprint_tube
reload (blueprint_tube)


""" Set this up so we have a string to query. """
""" That string is the class name so we can later say import.(the value from class name) """
CLASS_NAME = "Hinge"

""" Here is all the info we are querying when we import this into rigTool_UI """
TITLE = "Hinge"
DESCRIPTION = "Creates a hinge layout object.  Good for arms. "
ICON = os.environ["RIGTOOL"] + "/System/icons/hinge.bmp"

class Hinge:

    def __init__(self):  
        print 'init'
        self.buildHinge()


    def buildHinge(self):  
        
        """Create blueprint_sphere"""
        name = 'blueprint_sphere1'
        blueprint_sphere.blueprintSphere(name)
        name = 'blueprint_sphere1'
        blueprint_sphere.blueprintSphere(name)
        name = 'blueprint_sphere1'
        blueprint_sphere.blueprintSphere(name)
        
        """Create blueprint_tube"""
        name = 'blueprint_tube1'
        blueprint_tube.blueprintTube(name)
        name = 'blueprint_tube1'
        blueprint_tube.blueprintTube(name)
        
        """Create parenting hierarchy for sphere geo"""   
        cmds.parent('blueprint_sphere2', 'blueprint_sphere1')
        cmds.parent('blueprint_sphere3', 'blueprint_sphere2')
        
        geo = ['blueprint_sphere1', 'blueprint_sphere2', 'blueprint_sphere3', 'blueprint_tube1', 'blueprint_tube2']
        
        """Group the geo together"""
        cmds.group(geo[0], geo[3], geo[4], name = 'hingeGeo_grp')
