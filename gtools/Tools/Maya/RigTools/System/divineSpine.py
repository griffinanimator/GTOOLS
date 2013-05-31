# Create an empty list to store the lyt objects
lytObs=[]

# Get the layout objects into a list
lytRoot = cmds.ls(sl=True)
print lytRoot

# List the children of the root
children = cmds.listRelatives(lytRoot, allDescendents=True, type='transform')
print children

# Append each child to lytObs[]. Also get the position of each object as well as the parent
for child in children:
    lytPos = cmds.xform(child, q=True, t=True, ws=True)
    lytParent = cmds.listRelatives(child, parent=True, type='transform')
    lytObs.append([child, lytParent, lytPos])
# Append the root
lytPos = cmds.xform(lytRoot, q=True, t=True, ws=True)
lytObs.append([lytRoot[0], 'None', lytPos])

print lytObs

# Create 2 joint chains from the layout objects
for each in lytObs:
    print each[0]
    iksName = each[0].replace('lyt_', 'iksJnt_')
    cmds.select(d=True)
    cmds.joint(name=iksName, p=each[2])
    cmds.select(d=True)

# Draw a splineIK from the root to the last iksJnt.

# Create a new joint at the root and the top of the iksJoint chain.

# Bind the splineIK curve to those 2 new joints.