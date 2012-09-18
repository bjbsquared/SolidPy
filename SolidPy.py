import string
import copy

def inches(x):
    return 25.4*x

def boolStr(abool):
    """retuns a lower case string of 'true' or 'false'"""
    if abool: #OSCad needs lower case
        return "true"
    else:
        return "false"

def isVector(v):
    """Test to see if it is like [x,y,z]"""
    if type(v)==list and len(v)==3:
        return True

def Use(fileName):

    try:
        module = open(fileName)
        contents = module.read()
        module.close()
    except IOError:
        raise Exception( "Failed to include SCAD module '%s'"%fileName)
    else:
        SolidPyObj.includeFiles.append(fileName)

##def Use(fileName):





class SolidPyObj(object):
    _tab = " "*4
    includeFiles=[]
    fs=None
    fn=None
    fa=None
    autoColor = False
    colors=["red","blue","green","orange","yellow","SpringGreen",
            "blue","purple","DarkOrchid","MistyRose"]
    colorCnt=0
##resistor color codes good for troubleshooting...
##    colors=["black","brown","red","orange","yellow","green",
##            "blue","purple","grey","white"]

    def __init__(self):
        self._transformStack = []
        self.root = False
        self.disable = False
        self.parent= None
        self.background = False
        self.debug = False
        self.comment = ""
        self._tabLvl =0
        if SolidPyObj.autoColor:
            self.color(SolidPyObj.colors[SolidPyObj.colorCnt%len(SolidPyObj.colors)])
            SolidPyObj.colorCnt +=1

#ToDo add __str__ to Solid object model

    def __add__(self,solidPyObj1):
            """a=x+y calls x.__add__(y)->a"""
            if isinstance(self,Union):
                self.add(solidPyObj1)
                return self

            elif isinstance(solidPyObj1,Union):
                solidPyObj1.add(self)
                return solidPyObj1
            else:
                newUnion = Union(self,solidPyObj1)
                return newUnion

    def __sub__(self, solidPyObj1):
            if isinstance(self,Difference):
                self.add(solidPyObj1)
                return self
            else:
                newDifference = Difference(self,solidPyObj1)
                return newDifference

    def __mul__(self, solidPyObj1):
            if isinstance(self,Intersection):
                self.add(solidPyObj1)
                return self
            if isinstance(solidPyObj1,Intersection):
                solidPyObj1.add(self)
                return solidPyObj1
            else:
                newIntersection = Intersection(self,solidPyObj1)
                return newIntersection

    def copy(self):
        return copy.deepcopy(self)

    def set__tabLvl(self,lvl):
        self._tabLvl =lvl

    def rotate(self,x,y=None,z=None, v = None):
        """Puts a rotate transform on the transform stack"""
        rStr =""
        if type(x) == list:
            loc=x
        else:
            if not y or not z:
                loc=[x,x,x]
            else:
                loc=[x,y,z]
            x,y,z=loc

        if v:
            q,r,s=v
            rStr = "rotate(a = [%.2f,%.2f,%.2f], v = [%.2f,%.2f,%.2f])"%(1.0*x,1.0*y,1.0*z,1.0*q,1.0*r,1.0*s)
        else:
            rStr = "rotate(%s)"%str(loc)
        self._transformStack.append(rStr)

    def release(self):
        if self.parent:
            self.parent.children.remove(self)
            self.parent=None
            self._tabLvl = 0

    def scale(self,x,y=None,z=None):
        """Puts a scale transform on the transform stack"""
        if type(x) == list:
            loc=x
        else:
            if not y or not z:
                loc=[x,x,x]
            else:
                loc=[x,y,z]
            x,y,z=loc
            rStr = "scale([%.2f,%.2f,%.2f])"%(1.0*x,1.0*y,1.0*z)
            self._transformStack.append(rStr)

    def translate(self,x,y=None,z=None):
        """
        Puts a translate transform on the transform stack
        translate( [x,y,z]) or translate(x,y,z)
        translate (1) -> [1,1,1]
    """

        if type(x) == list:
            loc=x
        else:
            if not y or not z:
                loc=[x,x,x]
            else:
                loc=[x,y,z]

        x,y,z=loc
        rStr = "translate([%.2f,%.2f,%.2f])"%(1.0*x,1.0*y,1.0*z)
        self._transformStack.append(rStr)

    def mirror(self,x,y=None,z=None):
        """Puts a mirror transform on the transform stack
        mirror( [x,y,z]) or mirror(x,y,z)
        mirror (1) -> [1,1,1]
        """
        if type(x) == list:
            loc=x
        else:
            if not y or not z:
                loc=[x,x,x]
            else:
                loc=[x,y,z]
        x,y,z=loc
        rStr = "mirror([%.2f,%.2f,%.2f])"%(1.0*x,1.0*y,1.0*z)
        if isVector(v):
            self._transformStack.append(rStr)

    def multmatrix(self,m):
        """Puts a multmatrix transform on the transform stack
        *** not tested ***"""
        rStr = "multmatrix(%s)"%str(m)
        self._transformStack.append(rStr)

    def color(self,color = "yellow",alpha=1.0):
        self.color = color
        self.alpha = alpha
        if type(color) == str:
            rStr = 'color("%s", %s)' %(color,str(alpha))
            self._transformStack.append(rStr)

        if type(color) == list:
            rStr = 'color(%s, %s)' %(str(color),str(alpha))
            self._transformStack.append(rStr)

    def OSCString(self, protoStr):
        """Returns the OpenSCAD string to make the object"""
        #look for any modifiers
        OSCstr =""

        for each in self._transformStack:
            OSCstr = each + " " + OSCstr

        modStr =""
        if self.background:
            modStr+="%"
        if self.debug:
            modStr+="#"
        if self.disable:
            modStr+="!"
        if self.root:
            modStr+="*"
        OSCstr =+ self._tabLvl*SolidPyObj._tab + modStr+OSCstr

        OSCstr += protoStr

        if self.comment !="":
            OSCstr += " //%s\n"%self.comment
        else:
            OSCstr += "\n"

        return OSCstr


class Cube(SolidPyObj):
    """
    Cube( [x,y,z],center=True) or Cube( x,y,z,center)
    size = 1 -> [1,1,1]
    center: If True, object is centered at (0,0,0)
    """
##    def __init__(self, size = [1,1,1], center = False)
    def __init__(self,x,y=None,z=None,center=False):
        SolidPyObj.__init__(self)
        if type(x) == list:
            self.size=x
        else:
            if not y:
                self.size=[x,x,x]
            else:
                self.size=[x,y,z]

        self.center = center

    def renderOSC(self):
        protoStr = "cube(size=%s, center=%s);"%(self.size,boolStr(self.center))
        return self.OSCString(protoStr)

class Sphere(SolidPyObj):
    """
    rad=radius
    fa = Angle in degrees
    fs= Angle in mm
    center: If True, object is centered at (0,0,0)
    """
    def __init__(self,rad,fa=None,fs=None,fn=None):
        SolidPyObj.__init__(self)
        self.rad = rad
        self.fa = SolidPyObj.fa
        self.fa = fa
        self.fa = fs
        self.fa = fn

    def renderOSC(self):
        protoStr = "sphere(r = %s"%str(self.rad)
        if self.fa:
            protoStr += ", $fa = %s"%str(self.fa)
        if self.fs:
            protoStr += ", $fs = %s"%str(self.fs)
        if self.fn:
            protoStr += ", $fn = %s"%str(self.fn)
        protoStr += ");"
        return self.OSCString(protoStr)

class Cylinder(SolidPyObj):
    def __init__(self,h,rad,r2=None,fa=None,fs=None,fn=None, center=None):
        """
        h= height, rad=radius note if r2 == None->r2=rad
        fa = Angle in degrees
        fs= Angle in mm
        center: If True, object is centered at (0,0,0)
        """
        SolidPyObj.__init__(self)
        self.rad = rad
        self.h =h
        self.r2=r2
        self.fa = fa
        self.fa = fs
        self.fa = fn
        self.center = center

    def renderOSC(self):
        if not self.r2:
            protoStr ="cylinder(h=%s, r=%s"%(str(self.h),str(self.rad))
        else:
            protoStr = "cylinder(h=%s, r1=%s, r2=%s"%(str(self.h),str(self.rad),str(self.r2))

        if self.fa:
            protoStr += ", $fa = %s"%str(self.fa)
        if self.fs:
            protoStr += ", $fs = %s"%str(self.fs)
        if self.fn:
            protoStr += ", $fn = %s"%str(self.fn)
        if self.center:
            protoStr += ", center = %s"%boolStr(self.center)
        protoStr += ");"
        return self.OSCString(protoStr)

class Polyhedron(SolidPyObj):
    def __init__(self,points,triangles):
        SolidPyObj.__init__(self)
        self.points = points
        self.triangles = triangles

    def renderOSC(self):
        protoStr = ""
        protoStr += "polyhedron(points = %s,\n triangles = %s);"%(str(self.points), str(self.triangles))
        return self.OSCString(protoStr)

class Linear_extrude(SolidPyObj):
    def __init__ (self,flatPyObj,height,center=None,convexity=None,twist=None):
        SolidPyObj.__init__(self)
        self.flatPyObj = flatPyObj
        self.height = height
        self.center = center
        self.convexity= convexity
        self.twist=twist

    def renderOSC(self):
        protoStr ="linear_extrude(height=%s"%self.height
        if self.center:
            protoStr += ", center = %s"%boolStr(self.center)
        if self.convexity:
            protoStr += ", convexity = %s"%self.convexity
        if self.twist:
            protoStr += ", twist = %s"%self.twist
        protoStr += ") "
        protoStr += self.flatPyObj.renderOSC()
        return self.OSCString(protoStr)


class Rotate_extrude(SolidPyObj):
    def __init__ (self,flatPyObj,convexity=None,fn=None):

        SolidPyObj.__init__(self)
        self.flatPyObj = flatPyObj
        self.convexity = convexity
        self.fn = fn


    def renderOSC(self):
        protoStr ="rotate_extrude("
        if self.convexity:
            protoStr+=" convexity=%s"%self.convexity
        if self.fn:
            protoStr += ", fn = %s"%self.fn
        protoStr += ") "
        protoStr += self.flatPyObj.renderOSC()
        return self.OSCString(protoStr)

##projection(cut = true)
class Projection(SolidPyObj):
    def __init__ (self,flatPyObj,cut):

        SolidPyObj.__init__(self)
        self.flatPyObj = flatPyObj
        self.cut = cut

    def renderOSC(self):
        protoStr ="projection(cut=%s)"%self.cut
        protoStr += self.flatPyObj.renderOSC()
        return self.OSCString(protoStr)

class Import(SolidPyObj):
    def __init__(self,filename):
        SolidPyObj.__init__(self)
        self.filename = filename

    def renderOSC(self):
        protoStr = ""
        protoStr += 'import("%s");'%self.filename
        return self.OSCString(protoStr)


class Circle(SolidPyObj):
    def __init__(self,r,fn=None):
        SolidPyObj.__init__(self)
        self.fn = fn
        self.r = r

    def renderOSC(self):
        protoStr = "" + self._tabLvl*SolidPyObj._tab
        protoStr += "circle(r = %s"%self.r
        if self.fn:
            protoStr+=", $fn=%s"%self.fn
        protoStr+=");"
        return self.OSCString(protoStr)

class Square(SolidPyObj):
    def __init__(self,x,y,center=None):
        SolidPyObj.__init__(self)
        self.size = [x,y]
        self.center = center

    def renderOSC(self):
        protoStr = ""
        protoStr += "square(%s"%self.size
        if self.center:
            protoStr += ", center = %s"%boolStr(self.center)
        protoStr+=");"
        return self.OSCString(protoStr)

class Polygon(SolidPyObj):
    def __init__(self,points,paths=None, convexity=None):
        SolidPyObj.__init__(self)
        self.points = points
        self.paths = paths
        self.convexity =convexity

    def renderOSC(self):
        protoStr = ""
        protoStr += "polygon(points=%s"%self.points
        if self.paths:
            protoStr += ", paths= %s"%self.paths
        if self.convexity:
            protoStr += ", convexity= %s"%self.convexity
        protoStr+=");"
        return self.OSCString(protoStr)



class Import_dxf(SolidPyObj):
    def __init__(self,filename,layer=None,origin=None,scale=None):
        SolidPyObj.__init__(self)
        self.filename =filename
        self.layer =layer
        self.origin=origin
        self.scale=scale

    def renderOSC(self):
        protoStr = ""
        protoStr += 'import_dxf(file="%s"'%self.filename
        if self.layer:
            protoStr += ", layername = %s"%self.layer
        if self.origin:
            protoStr += ", origin = %s"%self.origin
        if self.scale:
            protoStr += ", scale = %s"%self.scale
        protoStr+=");"
        return self.OSCString(protoStr)

##dxf_linear_extrude(file="finn.dxf", height=3, convexity=1, center=true);
class DXF_linear_extrude(SolidPyObj):
    def __init__(self,filename,height,convexity=None,center=None):
        SolidPyObj.__init__(self)
        self.filename =filename
        self.height =height
        self.convexity =convexity
        self.center=center

    def renderOSC(self):
        protoStr = ""
        protoStr += 'dxf_linear_extrude(file="%s"'%self.filename
        if self.height:
            protoStr += ", height=%s"%self.height
        if self.convexity:
            protoStr += ", convexity=%s"%self.convexity
        if self.center:
            protoStr += ", center=%s"%boolStr(self.center)
        protoStr+=");"
        return self.OSCString(protoStr)


########### CGS Modeling ################

class CGS(SolidPyObj):
    """Generic class that other CGS classes inherit from. Will accept
    lists or individual solid objects."""
    def __init__(self,solidPyObj1,solidPyObj2):
        SolidPyObj.__init__(self)
        self.children=[]

        if type(solidPyObj1)== list:
            for solid in solidPyObj1:
                self.add(solid)
        elif solidPyObj1:
            self.add(solidPyObj1)

        if type(solidPyObj2)== list:
            for solid in solidPyObj2:
                self.add(solid)
        elif solidPyObj2:
            self.add(solidPyObj2)

    def add(self,solidPyObj1):

        solidPyObj1.release()
        solidPyObj1.set__tabLvl(self._tabLvl+1)
        solidPyObj1.parent = self
        self.children.append(solidPyObj1)

    def set__tabLvl(self,lvl):
        self._tabLvl = lvl
        for child in self.children:
            child.set__tabLvl(lvl+1)

    def renderOSC(self,protoStr):
        childrenStr =""
        for child in self.children:
            childrenStr += child.renderOSC()
        childrenStr += self._tabLvl*SolidPyObj._tab+"}\n"

        return self.OSCString(protoStr+childrenStr)

class Union(CGS):
    def __init__(self,solidPyObj1=None,solidPyObj2=None):

        CGS.__init__(self,solidPyObj1,solidPyObj2)


    def renderOSC(self):
       return CGS.renderOSC(self,"union() {\n")

class Difference(CGS):
    def __init__(self,solidPyObj1=None,solidPyObj2=None):
        CGS.__init__(self,solidPyObj1,solidPyObj2)

    def renderOSC(self):
       return CGS.renderOSC(self,"difference() {\n")

class Intersection(CGS):
    def __init__(self,solidPyObj1=None,solidPyObj2=None):

        CGS.__init__(self,solidPyObj1,solidPyObj2)

    def renderOSC(self):
       return CGS.renderOSC(self,"intersection() {\n")

class Minkowski(CGS):
    def __init__(self,solidPyObj1=None,solidPyObj2=None):

        CGS.__init__(self,solidPyObj1,solidPyObj2)

    def renderOSC(self):
       return CGS.renderOSC(self,"minkowski() {\n")

class Hull(CGS):
    def __init__(self,solidPyObj1=None,solidPyObj2=None):

        CGS.__init__(self,solidPyObj1,solidPyObj2)

    def renderOSC(self):
       return CGS.renderOSC(self,"hull() {\n")

class Module(SolidPyObj):
    def __init__(self,name,*arg):
        self.name=name
        self.arg=arg
        SolidPyObj.__init__(self)

    def renderOSC(self):
        protoStr = "" + self._tabLvl*SolidPyObj._tab
        protoStr += "%s%s;"%(self.name,self.arg)
        return self.OSCString(protoStr)

def writeSCADfile(fileName,rootObj,render=False):
    theStr=""

    for f in SolidPyObj.includeFiles:
        theStr += "use<%s>;\n\n"%f
    if SolidPyObj.fa:
        theStr +='$fa=%s;\n'%SolidPyObj.fa
    if SolidPyObj.fn:
        theStr +='$fn=%s;\n'%SolidPyObj.fn
    if SolidPyObj.fs:
        theStr +='$fs=%s;\n'%SolidPyObj.fs

    theStr +='\n'
    theStr += rootObj.renderOSC()

    if render:
        theStr = 'render(convexity = 1){\n%s\n}'%theStr
    outF=open(fileName, 'w')

    outF.write(theStr)

    outF.close

def main():

    Use("ring.scad")

    g = Module("ring",5,5,10)

    writeSCADfile('solidPy.scad',g)

    print g.renderOSC()


if __name__ == '__main__':
    main()
