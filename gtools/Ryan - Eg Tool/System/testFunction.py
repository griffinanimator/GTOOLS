import maya.cmds as cmds
import os
import sys   

    
class TestFunc:
    """ Lets use the __init__function to declare some variables """
    def __init__(self, info):
        print 'In TestFunc'
        print info