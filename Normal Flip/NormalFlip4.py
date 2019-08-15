import maya.cmds as cmds
import maya.mel as mel

mesh_list = cmds.ls(sl=1)

def faceNormal(mesh_list):
	face_normal = cmds.polyInfo(mesh_list, fn=True)
	for normal in  face_normal:
		position_normal = normal.split(' ')
		z = position_normal[-1]
		y = position_normal[-2]
		x = position_normal[-3] 
		faceID = position_normal[-4]
		print faceID,x ,y ,z

faceNormal(mesh_list)