import pymel.core as pm
 
def getBuildOrder(face):
	"""Returns the uvs of a face in the build order """
	verts = []
	vtxFaces = pm.ls(pm.polyListComponentConversion(face, toVertexFace=True), flatten=True)
	for vtxFace in vtxFaces:
		uvs = pm.polyListComponentConversion(vtxFace, fromVertexFace=True, toUV=True)
		verts.append(uvs[0])
	return verts
 
def getUVFaceNormal(face):
	"""Returns the UV normals from face"""
	uvs = getBuildOrder(face)
	#print ("uvs are : " + str(uvs))
	#ignore non-valid faces
	if len(uvs) < 3:
		return 1, 0, 0
	#get uvs positions:
	uvA_xyz = pm.polyEditUV(uvs[0], query=True, uValue=True, vValue=True)
	uvB_xyz = pm.polyEditUV(uvs[1], query=True, uValue=True, vValue=True)
	uvC_xyz = pm.polyEditUV(uvs[2], query=True, uValue=True, vValue=True)
	#print uvA_xyz, uvB_xyz, uvC_xyz
	#get edge vector
	uvAB = pm.dt.Vector([uvB_xyz[0]-uvA_xyz[0], uvB_xyz[1]-uvA_xyz[1], 0])
	uvBC = pm.dt.Vector([uvC_xyz[0]-uvB_xyz[0], uvC_xyz[1]-uvB_xyz[1], 0])
	#cross product & normalize
	uvNormal = uvAB.cross(uvBC)
	uvNormal = uvNormal.normal()
	return uvNormal
 
def findReversed(obj):
	"""Returns meshes with normals pointing inward"""
	reverseds = []
 
	#Convert to faces, then to vertexFaces:
	faces = pm.polyListComponentConversion(obj, toFace=True)
	faces = pm.ls(faces, flatten=True)
	for face in faces:
		uv_normal = getUVFaceNormal(face)
		#print ("uvNormal: " + str(uv_normal))
		#if the uv face normal is facing into screen then its reversed - add it to the list
		if (uv_normal * pm.dt.Vector([0, 0, 1])) < 0:
			reversed.append(face)
	return reverseds
	pass
 
# Run the command:
sel = pm.ls(selection=True)
reversed_meshes = []
for object in sel:
	#Conform object before looking for reversed faces:
	pm.polyNormal(sel, normalMode=2, userNormalMode=0,  ch=1)
	reverseds = findReversed(object)
	if reverseds:
		reversed_meshes.append(object)
print "reversed meshes: " + str(reversed_meshes)
 
for mesh in reversed_meshes:
	print mesh
	pm.polyNormal(mesh, normalMode=0, userNormalMode=0,  ch=1)
pm.select(sel)