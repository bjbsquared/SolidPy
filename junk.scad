
translate([43.30,25.00,15.00]) color("purple", 1.0) sphere(r = 2);

translate([42.86,25.75,15.00]) color("DarkOrchid", 1.0) sphere(r = 2);

translate([42.40,26.50,15.00]) color("MistyRose", 1.0) sphere(r = 2);

translate([41.93,27.23,15.00]) color("blue", 1.0) sphere(r = 2);

translate([41.45,27.96,15.00]) color("green", 1.0) sphere(r = 2);

translate([40.96,28.68,15.00]) color("orange", 1.0) sphere(r = 2);

translate([40.45,29.39,15.00]) color("yellow", 1.0) sphere(r = 2);

translate([39.93,30.09,15.00]) color("SpringGreen", 1.0) sphere(r = 2);

translate([39.40,30.78,15.00]) color("purple", 1.0) sphere(r = 2);

translate([38.86,31.47,15.00]) color("DarkOrchid", 1.0) sphere(r = 2);

translate([38.30,32.14,15.00]) color("MistyRose", 1.0) sphere(r = 2);

translate([37.74,32.80,15.00]) color("blue", 1.0) sphere(r = 2);

translate([37.16,33.46,15.00]) color("green", 1.0) sphere(r = 2);

translate([36.57,34.10,15.00]) color("orange", 1.0) sphere(r = 2);

translate([35.97,34.73,15.00]) color("yellow", 1.0) sphere(r = 2);

translate([35.36,35.36,15.00]) color("SpringGreen", 1.0) sphere(r = 2);

translate([34.73,35.97,15.00]) color("purple", 1.0) sphere(r = 2);

translate([34.10,36.57,15.00]) color("DarkOrchid", 1.0) sphere(r = 2);

translate([33.46,37.16,15.00]) color("MistyRose", 1.0) sphere(r = 2);

translate([32.80,37.74,15.00]) color("blue", 1.0) sphere(r = 2);

translate([32.14,38.30,15.00]) color("green", 1.0) sphere(r = 2);

translate([31.47,38.86,15.00]) color("orange", 1.0) sphere(r = 2);

translate([30.78,39.40,15.00]) color("yellow", 1.0) sphere(r = 2);

translate([30.09,39.93,15.00]) color("SpringGreen", 1.0) sphere(r = 2);

translate([29.39,40.45,15.00]) color("purple", 1.0) sphere(r = 2);

translate([28.68,40.96,15.00]) color("DarkOrchid", 1.0) sphere(r = 2);

translate([27.96,41.45,15.00]) color("MistyRose", 1.0) sphere(r = 2);

translate([27.23,41.93,15.00]) color("blue", 1.0) sphere(r = 2);

translate([26.50,42.40,15.00]) color("green", 1.0) sphere(r = 2);

translate([25.75,42.86,15.00]) color("orange", 1.0) sphere(r = 2);

color("yellow", 1.0) intersection() {
    color("blue", 1.0) cylinder(h=15, r=50);
    color("orange", 1.0) linear_extrude(height=20) color("green", 1.0) polygon(points=[[0, 0], [51.96152422706632, 29.999999999999996], [30.000000000000007, 51.96152422706631]]);

}


