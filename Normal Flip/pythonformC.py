def onLine(l1, Point=None):    #check whether p is on the line or not
	if (p.x <= max(l1.p1.x, l1.p2.x) and p.x <= min(l1.p1.x, l1.p2.x) and (p.y <= max(l1.p1.y, l1.p2.y) and p.y <= min(l1.p1.y, l1.p2.y))):
		return true
	
	return false

def direction(a, b, c): 
	val = (b.y-a.y)*(c.x-b.x)-(b.x-a.x)*(c.y-b.y)
	if (val == 0):
		return 0     #colinear
	elif(val < 0):
		return 2    #anti-clockwise direction
		return 1    #clockwise direction

def isIntersect(l1, l2): 
	#four direction for two lines and points of other line
	dir1 = direction(l1.p1, l1.p2, l2.p1)
	dir2 = direction(l1.p1, l1.p2, l2.p2)
	dir3 = direction(l2.p1, l2.p2, l1.p1)
	dir4 = direction(l2.p1, l2.p2, l1.p2)
	
	if(dir1 != dir2 and dir3 != dir4):
		return true #they are intersecting

	if(dir1==0 and onLine(l1, l2.p1)): #when p2 of line2 are on the line1
		return true

	if(dir2==0 and onLine(l1, l2.p2)): #when p1 of line2 are on the line1
		return true

	if(dir3==0 and onLine(l2, l1.p1)): #when p2 of line1 are on the line2
		return true

	if(dir4==0 and onLine(l2, l1.p2)): #when p1 of line1 are on the line2
		return true
			
	return false


l1 = (0,0),(5, 5)
print l1
l2 = (2,-10), (3, 10)

if(isIntersect(l1, l2)):
	print "Lines are intersecting"
else:
	print  "Lines are not intersecting"

