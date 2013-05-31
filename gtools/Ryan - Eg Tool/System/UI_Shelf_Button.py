import os
import sys

try:
    riggingToolRoot = os.environ["RIGTOOL"]
except:
    print "RIGTOOL environment variable not correctly configured"
else: 
    print riggingToolRoot
    path = riggingToolRoot

    if not path in sys.path:
        sys.path.append(path)

    import System.rigTool_UI as rigTool_UI
    reload (rigTool_UI)

    
    UI = rigTool_UI.RigTool_UI()