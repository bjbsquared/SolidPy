
union() {
    difference() {
        cube(size=[20.0, 20.0, 10.0], center=true);
        translate([0.00,0.00,1.00]) cube(size=[19.0, 19.0, 10.0], center=true);
    }

    translate([30.00,0.00,0.00]) rotate([180, 0, 0]) union() {
        translate([0.00,0.00,1.00]) cube(size=[24.0, 24.0, 1.0], center=true);
        color("red", 0.5) difference() {
            cube(size=[22.0, 22.0, 2.0], center=true);
            cube(size=[20.25, 20.25, 4.0], center=true);
        }

    }

}


