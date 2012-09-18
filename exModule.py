from SolidPy import *

def main():
    Use("parametric_involute_gear_v5.0.scad")
  
    junk=Module("gear",
               circular_pitch=700,
               gear_thickness = 12,
               rim_thickness = 15,
               hub_thickness = 17,
               circles=6)
    
    writeSCADfile('junk.scad',junk)

if __name__ == '__main__':
    main()