
module rachetTooth(ht = 1, thk=1,ra = 20, ba = 60){
//	ra = ramp angle
//	ba = back angle
//	ht = height
	
	xh = ht/tan(ra);
	xb = xh - ht*sin(90-ba);
	//echo(xh);
	rotate([0,0,90])
	translate([0,thk/2,0])
	rotate([90,0,0])
	translate([-xh/2,0,0])
	linear_extrude(height = 1) polygon(points=[[0,0],[xh,ht],[xb,0]]);
}
rachetTooth();