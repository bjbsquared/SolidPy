from SolidPy import *
from math import sin,cos,radians

Defaults.autoColor = True

def xy(magnitude,degrees):
    x= 1.0*magnitude*cos(radians(degrees))
    y= 1.0*magnitude*sin(radians(degrees))
    return[x,y]


pie = Cylinder(h = 15, r = 50)

slicer = Polygon([[0,0],xy(60,30),xy(60,60)]);

slicer = Linear_extrude(slicer,20)

pieSlice = pie*slicer

crumb = Sphere(r = 2)
x,y = xy(60,30)
crumb.translate(x, y, 15)

crust = []

for i in range(30, 60):
    crumb = Sphere(r = 2)
    x, y = xy(50, i)
    crumb.translate(x, y, 15)
    crust += [crumb]
    

writeSCADfile('junk.scad', crust, pieSlice)

# 
