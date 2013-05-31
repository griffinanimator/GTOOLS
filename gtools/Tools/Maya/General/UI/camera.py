# Import maya python command library
import maya.cmds as mc

# Define a window
window = mc.window(title='FaceCtrl_Window', w=800, h=1300)

#  Create a pane layout to store the modelPanel
cmds.paneLayout()

# The model panel can show a camera
cmds.modelPanel(camera='FacialCtrl_Cam' )

# Show the window
mc.showWindow(window)