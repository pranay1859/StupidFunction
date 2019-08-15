import pymel.core.datatypes as dt
import maya.cmds as cmds
from pymel.all import *

def checkFaceFlip(face_list):
	"""
	this function check every face in polgon and use vector to calculate face normals
	"""
	for face in face_list:
		uvs = []
		vtxFaces = cmds.ls(cmds.polyListComponentConversion(face, toVertexFace=True), flatten=True)
		for vtxFace in vtxFaces:
			uv = cmds.polyListComponentConversion(vtxFace, fromVertexFace=True, toUV=True)
			uvs.append( uv[0] )
		#get edge vectors and cross them to get the uv face normal
		uvAPos = cmds.polyEditUV(uvs[0], q=True)
		uvBPos = cmds.polyEditUV(uvs[1], q=True)
		uvCPos = cmds.polyEditUV(uvs[2], q=True)
		uvAB = dt.Vector([uvBPos[0] - uvAPos[0], uvBPos[1] - uvAPos[1]])
		uvBC = dt.Vector([uvCPos[0] - uvBPos[0], uvCPos[1] - uvBPos[1]])
		if not uvAB.cross(uvBC) * dt.Vector([0, 0, 1]) >= 0:
			#print face ### to check whick face is broken ###
			mesh = face.split('.')[0]
			return mesh

def flipNormals(mesh_list=None):
	"""
	list the selected create ,sets and run checkFaceFlip function
	"""
	if not mesh_list:
		mesh_list = cmds.ls(type='mesh')

	#mesh_list = cmds.ls(type='mesh') # list all scence
	mesh_list = cmds.ls(sl=True) # list selected
	cmds.select(cl=True)
	
	if not cmds.objExists("flipNormal"):
		cmds.sets(n="flipNormal")
		
	transform_list = cmds.listRelatives(mesh_list, parent=True, fullPath=True)
	poly_list = cmds.polyListComponentConversion(transform_list, tf=True)
	
	for poly in poly_list:
		face_list = cmds.ls(poly, flatten=True)
		mesh = checkFaceFlip(face_list)
		if not mesh:
			continue
		cmds.sets(mesh, e=True, add="flipNormal")
	print "Done"