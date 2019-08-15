import pymel.core as pm

def checkNegativeUV():
	massage, toSel = [], []
	geos = dict([(geo.nodeName(), geo) for geo in getAllGeoInGeoGrp()])
	for geo in geos.values():
		shape = geo.getShape(ni=True)
		currentUVSet = shape.getCurrentUVSetName()
		us, vs = shape.getUVs(currentUVSet)
		negUs = [u for u in us if u < 0]
		negVs = [v for v in vs if v < 0]
		if negUs or negVs:
			massage.append('{geo} has negative UV'.format(geo=geo))
			toSel.append(geo)

	if not toSel:
		return { checkNegativeUV.__name__ : True }

	negUVSetName = 'negativeUV_set'
	if pm.objExists(negUVSetName):
		pm.delete(negUVSetName)
	if massage:
		print ('\n'.join(massage))
		pm.sets(toSel, n=negUVSetName)

	return { checkNegativeUV.__name__ : toSel }
	
checkNegativeUV()