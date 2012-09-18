from SolidPy import *
class AxialFillet(object):
    def __init__(self,rfa,r):
        """
        rfa =  radius from axail
        r = radius of fillet
        axis= vector of axis
        """
        self.r=r
        self.rfa=rfa

    def outterFillet(self):
        """
        returns a SolidPyObject to cut with
        """
        c=Circle(self.r)
        c.translate([self.rfa-self.r,0,0])

        b=Square([self.r+1,self.r])
        b.translate([self.rfa-self.r+0.5,0,0])

        re=Rotate_extrude(b-c)
        re.translate([0,0,-self.r])
##        re.debug=True
        return re

    def innerFillet(self):
        """
        returns a SolidPyObject to cut with
        """
        c=Circle(self.r)
        c.translate([self.r+self.rfa,0,0])

        b=Square([self.r,self.r])
        b.translate([self.rfa,0,0])
        re=Rotate_extrude(b-c)
        re.translate([0,0,-self.r])

##        return b-c
        return re


def main():
    SolidPyObj.fs=0.1
##    SolidPyObj.fn = 60
##    SolidPyObj.fa = 6
    AF= AxialFillet(5,3)
    bb=AF.outterFillet()
    bb.translate([0,0,10])
##    bb.debug=True
    bb.color("red",0.5)
    aa=Cylinder(h=10,rad=5)
    aa.color("blue",0.5)
    junk= aa - bb

    writeSCADfile('junk.scad',junk)
if __name__ == '__main__':

    main()