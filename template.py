from SolidPy import *



def main():
    junk=Cylinder(h=10,rad=5)
    writeSCADfile('junk.scad',junk)

if __name__ == '__main__':
	main()