# SolidPy 
 
## Overview
[OSC]:http://www.openscad.org
[OSCUM]:http://en.wikibooks.org/wiki/OpenSCAD_User_Manual

SolidPy is a python module that allows generates [OpenSCAD][OSC] code from python code. The aim of developing this SolidPy is to simplify and enhance the design experience of code-based, parametric, solid modeling. 

Python + SolidPy -> OpenSCAD code -> Solid Model

##So, How do I use it?
Place SolidPy.py somewhere it your PYTHONPATH or in the directory of the python module that imports it. Write the python code to build your solid model. While your write your code and run it, changes to the output can be observed using OpenSCAD with the 'Automatic Reload and Compile' setting checked.

All the other files seen in the repository are working files that may be of help as examples. They may or may not work as SolidPy is undergoing changes.

## Language Differences
 *If some of this looks garbled see readme.html* 
 
 | SolidPy |Open SCAD|Difference |
 |:------- | :-------- | :--------- |
 | a = Sphere(r=2)| sphere(r=2) | First letter Capitalized |
 | b = Cube(1,2,3) | cube([1,2,3]) | Square brackets are optional |
 | b.color("red",0.5)|color("red",0.5) cube([1,2,3]) | Objects are transformed using methods |
 | b = a.copy()| no equivalent| Shapes are objects |
 | c = a + b |union(){sphere(r=2) cube([1,2,3])}| Easy to read syntax|
 

## Features
* Simple, flexible syntax
* Use of a Python IDE and the Python language is powerful 
* Treat objects like objects (not text)
* Use existing [OpenSCAD][OSC] modules
* Grow the object tree and pick the fruit you want (instead of taking the whole tree)
* AutoColoring mode
* Reference another solids attributes
* Copy shapes
* SolidPy Class can be extended to suit 


## SolidPy Classes
The SolidPy class was designed for maximum inheritance and flexibility. Each are named after the OpenSCAD they represent except the names are capitalized.

 Below shows the interface for each class. Treat the arguments for each just as they are for OpenSCAD. Of course there will be differences in syntax. Also some commands will allow a single object or a list of objects to be used as an argument. For specific OpenSCAD information see the [OpenSCAD Users Manual][OSCUM].


## Shapes
### Cube(self, x, y = None, z = None, center = None) or Cube(self, [x,y,z] center = None)
Returns a SolidPyObj which represents a cube. 

Examples: `myBox = Cube([3,4,5])` or `myBox = Cube(3,4,5)`


### Cylinder(h, r, r2 = None, fa = None, fs = None, fn = None, center = None)
Returns a SolidPyObj which represents a cylinder. 
       	 	
 example:    `myTube = Cylinder(h = 5, r=10, center = True )`
 
 
### Sphere(r, fa = None, fs = None, fn = None)
Returns a SolidPyObj which represents a cylinder. 

Notice that OpenSCAD uses **$**fs and **$**fn while SolidPy drops the **$**.

 example: `myBall = Sphere(r=5)`



### DXF_linear_extrude(filename, height, convexity = None, center = None)
Creates a 3D object by extruding a DXF file. Returns a SolidPyObj object.
 
   myShape = DXF_linear_extrude(mydxfFile, h=5)

   
### Linear_extrude(height,center,convexity,twist)
Extrudes shapes to make 3D object. Returns a SolidPyObj object.

### Import(fileName)
Imports a file for use in the current OpenSCAD model. Returns a SolidPyObj object.

### Module(moduleName,**kwargs) 
Calls a OpenSCAD Module brought in by the **Use(filename)** command. Arguments to the module must be given in keyworded values. Returns a SolidPyObj object.

    Use("Rachet Tooth.scad")

    tooth = Module("rachetTooth", ht = 1, thk=8, ra = 16, ba = 80)
    
### Polygon(pointsList, pathList, convexity)
Returns a SolidPyObj object.

###   Polyhedron(points,triangles) 

  Returns a SolidPyObj object.

### Projection(cut = true) 
  Returns a SolidPyObj object.

### Rotate_extrude(convexity = None, fn = None)
 Returns a SolidPyObj object.

### Square([x,y]) or Square(x, y)

## CGS Operations
CGS object hold other SolidPy objects as child objects. They perform the CGS operation on the child objects as described below.
 
### '+' Operator
### Union()
### Union([solidPyobjs])
### Union(solidObj1 = None, solidObj2 = None)


Union() returns an empty Union()  object that can be used to add SolidPy objects at a later time
Union ([objectList]) will create a union that contains the objects in [objectList]
Union ([objectList1], [objectList2]) will create a union that contains the objects in both lists.

An alternate form of Union is the  **'+'** operator.

    a = Cube(5,5,5)
    b = sphere(r = 6)
    myUnion = a + b
    
- If 'a' Union() then 'b' is added to the 'a' Union()
- If 'b' Union() then 'a' is added to the 'b' Union()
- If neither ''a or 'b' is a Union then both are added to a new union.

### '-' Operator
###Difference(solidObj1 = None, solidObj2 = None)
### Difference()
### Difference([solidPyobjs])

Difference() returns an empty Difference() that can be used to add SolidPy objects at a later time.
Difference ([objectList]) will create a Difference() that contains the objects in [objectList]
Difference ([objectList1], [objectList2]) will create a Difference() that contains the objects in both lists.
The first object added to the Difference() object is the one that all other will be subtracted from.

An alternate form of Union is the  **'-'** operator.

    a = Cube(5,5,5)
    b = sphere(r = 6)
    myDiff = a - b
    
- If 'a' is a Difference() then 'b' is subtracted from  the 'a' Difference()
- If 'a' is not a Difference() object a new is made placing 'a' as its first child from which 'b' will be subtracted.


### '*' Operator
###Intersection(solidObj1 = None, solidObj2 = None)
### Intersection()
### Intersection([solidPyobjs])

Intersection() returns an empty Intersection() that can be used to add SolidPy objects at a later time.
Intersection ([objectList]) will create an Intersection() that contains the objects in [objectList]
Intersection ([objectList1], [objectList2]) will create an Intersection that contains the objects in both lists.
The all objects added to the Intersection() object will define the intersection.

An alternate form of Union is the  **'*'** operator.

    a = Cube(5,5,5)
    b = sphere(r = 6)
    myIntersect = a * b
    
- If 'a' is an Intersection() then 'b' is intersected with the 'a' Intersection()
- If 'b' is an Intersection() then 'a' is intersected with the 'b' Intersection()
- If 'a' or 'b' are not  Intersection() objects, a new one is made.


### Minkowski( solidObj1 = None, solidObj2 = None)
Returns the Minkowski parent of solidObj1 and solidObj2.

### Hull(solidObj1 = None, solidObj2 = None)
Returns the Minkowski parent of solidObj1 and solidObj2.

##Transforms
Transforms are methods of SolidPy objects. Transforms are kept in the objects transform stack.
### translate(x,y,z)
###translate([x,y,z])
 | SolidPy |Open SCAD
 |:------- | :-------- |
 | a = Sphere(r=2)|sphere(r=2)
 | a.translate(2,4,6)| translate([2,4,6]){sphere(r=2)} 
 
 
### mirror(x,y,z)
### mirror([x,y,z])
 | SolidPy |Open SCAD
 |:------- | :-------- |
 | a = Sphere(r=2)|sphere(r=2)
 | a.translate(2,4,6)| translate([2,4,6]){sphere(r=2)} 

### multmatrix(m)
m is a 4x4 matrix.

 | SolidPy |Open SCAD
 |:------- | :-------- |
 | a = Sphere(r=2)|sphere(r=2)
 | a.multmatrix(m)| multmatrix(m){sphere(r=2)} 


### scale(x,y,z)
### scale([x,y,z])
 | SolidPy |Open SCAD
 |:------- | :-------- |
 | a = Sphere(r=2)|sphere(r=2)
 | a.scale(2,4,6)| scale([2,4,6]){sphere(r=2)} 
 
###color("color",alpha)
### color([r,g,b],alpha)
 | SolidPy |Open SCAD
 |:------- | :-------- |
 | a = Sphere(r=2)|sphere(r=2)
 | a.color("red", 0.5)| color("red", 0.5){sphere(r=2)} 

##Utility
### Comment
Each object can have a comment applied to  which will help identify it  in the OpenSCAD code. 

    a=Cube(1,2,3)
    a.comment = "Here is my Cube!"

###copy(SolidPyObj)
Copy creates an exact duplicate of the solid object except the parent of the duplicate is set to `None` and children are duplicates of the original.

     myBox = Cube(4,5,6)
	 myNewBox = myBox.copy()

###use("filename.scad")
This loads an OpenSCAD file in order to access modules within that file. 
Note that **include()** is not implemented.

###writeSCADfile(fileName, *args):
fileName = the SCAD file to save to. Include the '.scad' extension
*args can be SolidPy objects or lists of SolidPy objects.

###Extras
###inches(x)
Everything in OpenSCAD is assumed to be millimeters(mm). inches(X) returns 25.4 * X to 
convert x that is in inches to mm.
## Modifiers
Each object has modifiers that are found in OpenSCAD. They are boolean attributes.

* **root** 
* **disable**
* **background**
* **debug** 

Activate these as needed by:


      a = Cube(1,2,3)
      a.disable = True
    
##Defaults
Defaults are to be set by the user for their own taste.
###tab
By default 'Defaults.tab = " " * 4' This set the tab length in the OpenSCAD code written by writeSCADfile().

###includeFiles

Defaults.includeFiles is modified by the **Use(filename)** command to hold files to be included. It can also be modified directly.
###fs
Defaults.fs sets the Special Variable in OpenSCAD **$fs** at the beginning of the OpenSCAD file.
###fn
Defaults.fn sets the Special Variable in OpenSCAD **$fn** at the beginning of the OpenSCAD file.
###fa
Defaults.fa sets the Special Variable in OpenSCAD **$fa** at the beginning of the OpenSCAD file.
### autoColor
When `Default.autoColor == True` colors are automatically applied to all objects at their creation given by the order set in the Default.color[] list

###colors
Defaults.colors are used by the autoColor setting to automatically apply a color to a SolidPy object when it is created. 

    Defaults.colors = ["blue", "green", "orange", "yellow", "SpringGreen"]

Colors can be added or changed as required. Colors can be found at [OpenSCAD Users Manual][OSCUM].


