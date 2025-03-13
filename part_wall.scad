module part_left(args) {
    color("red", 0.2)
        rotate([90, 0, 0]) 
            cube([wall_x, wall_z, wall_t], center=true);
}

module part_right(args) {
    color("red", 0.2) 
        rotate([90, 0, 0]) 
            cube([wall_x, wall_z, wall_t], center=true);
}

module part_back(args) {
    color("red", 0.2) 
        rotate([0, 90, 0]) 
            cube([back_y_f, wall_z, wall_t], center=true);
}