import pymel.core.datatypes as dt
import maya.cmds as cmds
from pymel.all import *

def FlipNormals():
	'''this fuction list the'''
	# mesh_list = cmds.ls(type='mesh') 
	mesh_list = cmds.ls(sl=1)
	#print  '\nmesh on this scence is' , mesh_list

	transform_list = cmds.listRelatives(mesh_list, parent=True, fullPath=True)
	#print '\ntransformList on this scence is ', transform_list

	poly_list = cmds.polyListComponentConversion(transform_list, tf=True)
	#print '\npoly_list on this scence is ',poly_list

	for poly in poly_list:
		face_list = cmds.ls(poly, flatten=True)
		flip_mesh = checkFaceFlip(face_list)

	print "Done"

def checkFaceFlip(face_list):

	for face in face_list:
		uvs = []
		vtxFaces = cmds.ls(cmds.polyListComponentConversion(face,toVertexFace=True),flatten=True)
		for vtxFace in vtxFaces:
			uv = cmds.polyListComponentConversion(vtxFace,fromVertexFace=True,toUV=True)
			uvs.append( uv[0] )
		#get edge vectors and cross them to get the uv face normal
		uvAPos = cmds.polyEditUV(uvs[0], q=1)
		uvBPos = cmds.polyEditUV(uvs[1], q=1)
		uvCPos = cmds.polyEditUV(uvs[2], q=1)

		uvAB = dt.Vector([uvBPos[0] - uvAPos[0], uvBPos[1] - uvAPos[1]])
		uvBC = dt.Vector([uvCPos[0] - uvBPos[0], uvCPos[1] - uvBPos[1]])

		if not uvAB.cross(uvBC) * dt.Vector([0, 0, 1]) >= 0:
			# print face *** to check whick face is broken***
			mesh = face.split('.')[0]
			print mesh
			return 


FlipNormals()

'''
def FlipNormals():

	#mesh_list = cmds.ls(type='mesh')
	mesh_list = cmds.ls(sl=1)
	#print  '\nmesh on this scence is' , mesh_list

	transform_list = cmds.listRelatives(mesh_list, parent=True, fullPath=True)
	#print '\ntransformList on this scence is ', transform_list

	poly_list = cmds.polyListComponentConversion(transform_list, tf=True)
	#print '\npoly_list on this scence is ',poly_list

	for poly in poly_list:
		face_list = cmds.ls(poly, flatten=True)
		#print '\nface_list on this scence is ',face_list
		checkFaceFlip(face_list)
	print "Done"


def checkFaceFlip(face_list):

	for face in face_list:
		uvs = []
		vtxFaces = cmds.ls(cmds.polyListComponentConversion(face,toVertexFace=True),flatten=True)
		for vtxFace in vtxFaces:
			uv = cmds.polyListComponentConversion(vtxFace,fromVertexFace=True,toUV=True)
			uvs.append( uv[0] )
		#get edge vectors and cross them to get the uv face normal
		uvAPos = cmds.polyEditUV(uvs[0], q=1)
		#print uvAPos
		uvBPos = cmds.polyEditUV(uvs[1], q=1)
		#print uvBPos
		uvCPos = cmds.polyEditUV(uvs[2], q=1)
		#print uvCPos
		uvAB = dt.Vector([uvBPos[0] - uvAPos[0], uvBPos[1] - uvAPos[1]])
		#print uvAB
		uvBC = dt.Vector([uvCPos[0] - uvBPos[0], uvCPos[1] - uvBPos[1]])
		#print uvBC
		print  dt.Vector

		print  uvAB.cross(uvBC) * dt.Vector([0, 0, 1])

		if not uvAB.cross(uvBC) * dt.Vector([0, 0, 1]) >= 0:
			#print face
			mesh = face.split('.')[0]
			#print mesh
			#return 
'''

'''

import maya.cmds as cmds

face_normal = cmds.polyInfo( fn=True )

face_normal = face_normal[0].split(' ')
z = face_normal[-1]
y = face_normal[-2]
x = face_normal[-3] 
faceID = face_normal[-4]

print x,y,z,faceID

'''

# from pymel.all import *
# import pymel.core.datatypes as dt

# faces = ls((polyListComponentConversion((ls(fl=1,sl=1)), tf=1)), fl=1)

# for face in faces:
# 	uvs = []
# 	vtxFaces = ls(polyListComponentConversion(face,toVertexFace=True),flatten=True)
# 	for vtxFace in vtxFaces:
# 		uv = polyListComponentConversion(vtxFace,fromVertexFace=True,toUV=True)
# 		uvs.append( uv[0] )
# 	#get edge vectors and cross them to get the uv face normal
# 	uvAPos = polyEditUV(uvs[0], q=1)
# 	uvBPos = polyEditUV(uvs[1], q=1)
# 	uvCPos = polyEditUV(uvs[2], q=1)
# 	uvAB = dt.Vector([uvBPos[0]-uvAPos[0], uvBPos[1]-uvAPos[1]])
# 	uvBC = dt.Vector([uvCPos[0]-uvBPos[0], uvCPos[1]-uvBPos[1]])

# 	if not uvAB.cross(uvBC) * dt.Vector([0, 0, 1]) > 0: 
# 		print face,uvnormal


'''
import pymel.core.datatypes as dt
import maya.cmds as cmds
from pymel.all import *

def FlipNormals():

	"""
	list the selected and run checkFaceFlip function

	"""
	# mesh_list = cmds.ls(type='mesh')
	mesh_list = cmds.ls(sl=True)
	print  '\nmesh on this scence is' , mesh_list

	cmds.select(cl=True )

	cmds.sets(n="flipNormal")
		

	transform_list = cmds.listRelatives(mesh_list, parent=True, fullPath=True)
	print '\ntransformList on this scence is ', transform_list

	poly_list = cmds.polyListComponentConversion(transform_list, tf=True)
	print '\npoly_list on this scence is ',poly_list

	for poly in poly_list:
		face_list = cmds.ls(poly, flatten=True)
		print 'face_list', face_list
		checkFaceFlip(face_list)

	try:
		cmds.delete('flipNormal1')
	except:
		print "Done"

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
			#print mesh
			cmds.sets(mesh,e=True, add="flipNormal")
			return

FlipNormals()
'''