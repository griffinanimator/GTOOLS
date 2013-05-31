""" IK Controls.py """
""" garvey chi - 05-17-11 """
""" Functions for the creation of joints """

import maya.cmds as cmds
import csv

class Create_CSV:
    
    def createCSVfile(self):
        import System.csv_utils as csvUtils
        reload (csvUtils)
        csvWrite = csvUtils.csvWrite()
    
    def csvWrite():
    """ This is the path where the csv will be written.  Change this to a path on your local machine. """
    path = "C:/Users/Garvey/Documents/CSV_files/armCsv.csv" 
    
    """ Open the csv in maya for writing """
    writer = csv.writer(open(path, 'wb'), delimiter=',')
    
    """ Create a new list based off your selection """
    selectionList = cmds.ls(sl=True)
   
    """ Clear the selection """
    cmds.select(clear=True)
  
    for selection in selectionList:
        """ An empty list to hold both the joint names and the positions """
        jointInfo = []
  
        pos = cmds.xform(selection, q=True, t=True, ws=True)
       
        """ Append the name of the locator and it's position to a new list"""  
        """ I am splitting the positions into seperate variables to make things easier when I try read them later """     
        jointInfo.append(selection)
        jointInfo.append(pos[0])
        jointInfo.append(pos[1])
        jointInfo.append(pos[2])
        """ At this point you could use the joint info to build joints """
        """ Write the data to csv """
        writer.writerow(jointInfo)

    """ Print the joint info so you can see what is happening """
    print jointInfo