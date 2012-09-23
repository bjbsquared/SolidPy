from SolidPy import *


def main():
    innerD = 17.8
    outterD = innerD + 4
    length = 20

    foot = Cylinder(4, innerD / 3, center = True)
    foot.rotate([90, 0, 0])
    foot.translate([-7, 0, 0])
    foot.scale([1, 1, 1.65])

    body = Cylinder(length, outterD / 2, center = True) + foot
    body -= Cylinder(length + 5, innerD / 2, center = True)
    box = Cube([20, 25, 22], center = True)


    box.translate([13, 0, 0])
    body = body - box

    writeSCADfile('junk.scad', body)

if __name__ == '__main__':
    main()
