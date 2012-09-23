from SolidPy import *
from SolidPy import SolidPyObj

x = 20.0
y = 20.0
z = 10.0
t = 1.0 #thickenss
tol = 0.25
outter = [x, y, z]
inner = [x - t, y - t, z]

outerShell = Cube(outter, center = True)

innerShell = Cube(inner, center = True)

innerShell.translate([0, 0, t])

top = Cube([x + 4 * t, y + 4 * t, t], center = True)

top.translate([0, 0, t])
top.color("blue", 0.5)

rim = Cube([x + 2 * t, y + 2 * t, 2 * t],
            center = True) - Cube(x + tol, y + tol, 4 * t,
            center = True)
rim.color('red', 0.5)


top += rim
top.rotate([180, 0, 0])

box = outerShell - innerShell
top.translate(1.5 * x, 0, 0)
boxAndTop = Union(box, top)

writeSCADfile('junk.scad', boxAndTop)
##    writeSCADfile('junk.scad',top,render=True)


