// include <BOSL2/std.scad>

module part_bottom() {
    color("blue", 0.8)

        // 4. holders
        union() {}
            // 3. pocket
            difference() {
                linear_extrude(height=bottom_z, center=true)
                    union() {
                        // 1. create body
                        square([bottom_x, bottom_y], center=true);
                        // 2. add ears - module
                        union() {
                            translate([-ear_x_o, 0, 0]) bottom_ear();
                            translate([ear_x_o, 0, 0]) bottom_ear();
                        }
                    };
                translate([0, 0, bottom_t + 0.001]) cube(size=[bottom_x - bottom_t*2, bottom_y - bottom_t*2, bottom_po], center=true);
            }
            
            translate([-holder_x_o, holder_y_o, bottom_t / 2]) bottom_holder();
            translate([holder_x_o, holder_y_o, bottom_t / 2]) rotate([0, 0, -90]) bottom_holder();
            translate([holder_x_o, -holder_y_o, bottom_t / 2]) rotate([0, 0, 180]) bottom_holder();
            translate([-holder_x_o, -holder_y_o, bottom_t / 2]) rotate([0, 0, 90]) bottom_holder();

            translate([holder_x_o - ear_x - bottom_t, holder_y_o, bottom_t / 2]) cube([ear_x - bottom_t, bottom_t, bottom_po]);
            translate([holder_x_o - ear_x - bottom_t, -holder_y_o, bottom_t / 2]) cube([ear_x - bottom_t, bottom_t, bottom_po]);

                // front holder
                // 4 holders

                // bolts

                // lamp

}

module bottom_ear() {
    
    difference() {
        square(size=[ear_x, ear_y], center=true);
        square(size=[ear_x - bottom_t * 2, ear_y - bottom_t * 2], center=true);    
    }

}

module bottom_holder() {
    
    translate ([0, 0, 0]) difference() {
        cube(size=[holder_x, holder_x, bottom_po], center=true);
        translate([bottom_t, -bottom_t, 0]) cube(size=[holder_x, holder_x, bottom_po], center=true);
    }

}


module bottom_lamp() {
    // dif bolt 1
    // add bolt 2
    // dif lamp 1
    // dif lamp 2

}

