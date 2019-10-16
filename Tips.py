# print attrs from selected node
for i in maya.cmds.listAttr(http://maya.cmds.ls(sl=True)[0]):print(i)

# get file name without extention
from maya import cmds
file_name = (cmds.file(q=True, sn=True, shn=True)).split('.')[0]

# change working units to Centimeter
cmds.currentUnit(linear='cm')

# print Maya plug-in path
from maya import cmds, mel
path = mel.eval('getenv "MAYA_PLUG_IN_PATH"')
path_list = path.split(':')
for i in path_list:
    print i
    
