import math
from display import *



#vector functions
#normalize vector, should modify the parameter
def normalize(vector):
    pass

#Return the dot porduct of a . b
def dot_product(a, b):
    x0 = a[0]
    y0 = a[1]
    z0 = a[2]
    x1 = b[0]
    y1 = b[1]
    z1 = b[2]
    dp = x0 * x1 + y0 * y1 + z0 * z1
    return dp

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):
    return None
