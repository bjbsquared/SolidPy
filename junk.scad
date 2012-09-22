$fn=30;
$fs=0.1;

difference() {
    union() {
        cylinder(h=1.524, r=16.51);
        cylinder(h=26.416, r=5.08);
        translate([0.00,0.00,1.52]) rotate([180, 0, 0]) translate([0.00,0.00,-10.16]) rotate_extrude() difference() {
    translate([5.08,0.00,0.00]) square([10.16, 10.16]);
    translate([15.24,0.00,0.00])     circle(r = 10.16);
}


    }

    translate([0.00,0.00,26.42]) translate([0.00,0.00,-1.59]) rotate_extrude() difference() {
    translate([3.99,0.00,0.00]) square([2.5875, 1.5875]);
    translate([3.49,0.00,0.00])     circle(r = 1.5875);
}


    union() {
        translate([0.00,0.00,-1.00]) cylinder(h=1, r=3.7465, $fs = 0.1);
        cylinder(h=3.14368676821, r1=3.7465, r2=0.01, $fs = 0.1);
        cylinder(h=27.416, r=1.8923, $fs = 0.1);
    }

}


