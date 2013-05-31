import maya.cmds as cmds

class Example_UI:
    def __init__(self):
        """ Another Dictionary : ) """
        self.UIElements = {}
        
        
        """ Check to see if the window exists.  If True delete it.  If False, delete it. """
        if cmds.window("ExUI", exists=True):
            cmds.deleteUI("ExUI")
        
        
        """ Create a window"""
        cmds.window("ExUI", width=200, height=200)
        
        """ Make a layout.  Layouts are parented to the window and hold UI elements.
        A layout organizes the element in a defined way such as lining them up in a column """
        """ Add the layout to the UIElements dictionary """
        self.UIElements['flowLayout'] = cmds.flowLayout(visible=True, columnSpacing=5, w=200, h=200, v=True)
        
        self.UIElements['textField'] = cmds.textField(w=200, h=36, aie=True, text='Enter Some Text')
        
        cmds.button(label='get field val', width=200, height=66, visible=True, command=self.queryTextField)
        
        cmds.showWindow("ExUI")
        
    def queryTextField(self, *args):
        fieldVal = cmds.textField(self.UIElements['textField'], q=True, text=True)
        cmds.headsUpMessage( fieldVal )
        
        