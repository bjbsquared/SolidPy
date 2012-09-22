from SolidPy import *
from math import sin, cos, radians

def rectangular(magnitude,degrees):
    x= 1.0*magnitude*cos(radians(degrees))
    y= 1.0*magnitude*sin(radians(degrees))
    return[x,y]

Use("Rachet Tooth.scad")

##module rachetTooth(ht = 1, thk=1,ra = 20, ba = 60){
##//	ra = ramp angle
##//	ba = back angle
##//	ht = height

teeth=Union()
for ang in range(0,360,15):
    rad=12
    [x,y]=rectangular(rad,ang)
    tooth = Module("rachetTooth", ht = 1, thk = 1, ra = 17, ba = 80)
    tooth.rotate([0,90,0])
    tooth.rotate([0,0,ang])
    tooth.translate([x,y,0])
    teeth.add(tooth)
teeth.color('green')
core = Cylinder(h = 1, r = 1, center = True)
# core.debug=True
	
ratchet = teeth + core

writeSCADfile('ratchetGear.scad',ratchet)
def main():
    pass

if __name__ == '__main__':
    main()
