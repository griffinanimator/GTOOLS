import maya.cmds as cmds
import os
import sys   

import System.testFunction as testFunction
reload(testFunction)
    
class Test:
    """ Lets use the __init__function to declare some variables """
    def __init__(self):
        """ You can declare information about the module you are building """
        
        self.info = [ ['a', 'b'] ]
        
        self.dictionary = {}
        
        self.doStuf()
        
    def doStuff(self):
        self.dictionary['cats'] = (['black', 'white'])
        self.dictionary['dogs'] = (['big', 'small'])
        
        print self.dictionary['cats']
        print self.dictionary['dogs']
       
       