import maya.cmds as cmds
import os
import sys

def findAllModules(relativeDirectory):
    # search the relative directory  for all available modules
    # Return a list of all module names (excluding the ".py" extension)
    fileDirectory = os.environ["RIGTOOL"] + "/" + relativeDirectory + "/"
    allPyFiles = findAllFiles(relativeDirectory, fileDirectory, ".py")
    
    returnModules = []
    
    for file in allPyFiles:
        if file != "__init__":
            returnModules.append(file)
            
    return returnModules

def findAllFiles(relativeDirectory, fileDirectory, fileExtension):
    
    # Search the relative directory for all files with the given extension.
    # Return a list of all file names, excluding the file extension

    allFiles = os.listdir(fileDirectory)
    
    # Refine all files, listing only those of the specified file extension
    returnFiles = []
    for f in allFiles:
        splitString = str(f).rpartition(fileExtension)
        
        if not splitString[1] == "" and splitString[2] == "":
            returnFiles.append(splitString[0])

    return returnFiles