import pymel.core.datatypes as dt
import maya.cmds as cmds

def checkFaceFlip(face_list):
	'''
	this fuction check flip face by use .map[*] 
	return : flipface name and mesh name
	'''
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

		# if face is wrong direction
		if not uvAB.cross(uvBC) * dt.Vector([0, 0, 1]) >= 0:
			print face # show first face which broken
			mesh = face.split('.')[0]
			return mesh

def flipNormals(mesh_list=None):

	'''this fuction list the selected to list face and create set '''

	#select target
	mesh_list = cmds.ls(sl=1)

	if not mesh_list:
		mesh_list = cmds.ls(type='mesh')

	# clear select and create set
	cmds.select(cl=True)
	if not cmds.objExists('flipNormal'):
		cmds.sets(name='flipNormal')

	#list poly [u'pSphere1.f[*]', u'pCube1.f[*]', u'pCylinder1.f[*]']
	poly_list = cmds.polyListComponentConversion(mesh_list, tf=True)
	print poly_list

	# for poly poly_list 
	for poly in poly_list:
		face_list = cmds.ls(poly, flatten=True)
		mesh = checkFaceFlip(face_list)
		if not mesh:
			continue
		cmds.sets(mesh, e=True, add='flipNormal')

	print 'Done'

flipNormals()
