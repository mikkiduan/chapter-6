import math
biggest = max (3,7,10)
x = abs(3-7)

def area_sphere(r):
    return 4 * math.pi * r**2

def  dist3d(x1,y1,z1,x2,y2,z2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

def area_pts(x1,y1,z1,x2,y2,z2):
    r = dist3d(x1,y1,z1,x2,y2,z2)
    return area_sphere(r)

def is_divisible(x, y):
    """ Test if x is exactly divisible by y """
    return x % y == 0

    
#myval = abs_val(0)
#distomars = dist3d(0,0,0,2,3,6)
#area_mars = area_pts(0,0,0,2,3,6)