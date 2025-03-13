include <part_wall.scad>
include <part_bottom.scad>
// include <part_top.scad>
// include <part_front.scad>
// include <part_parts.scad>

// x - width, f - fix
// z - height
// t - thickness
// tol - tolerance
// d - diameter
// y - deep
// o - offset
// po - pocket
// r - radius

tol_f = 0.05;

back_y_f = 114; 
wall_x = back_y_f / 114 * 171;
wall_z = back_y_f;
wall_t = back_y_f / 114 * 1;
back_x_o = (wall_x - wall_t) / 2 ;
left_y_o = (back_y_f - - wall_t) / 2;

leg_x = back_y_f / 114 * 18;
leg_t = leg_x / 8;

bottom_t = back_y_f / 114 * 2;
bottom_z = back_y_f / 114 * 8;
bottom_x = wall_x + tol_f * 2 + bottom_t * 2;
bottom_y = back_y_f + (bottom_t + wall_t + tol_f) * 2;
bottom_po = bottom_z - bottom_t;
bottom_z_o = wall_z / 2 + bottom_t;

ear_leg_po_y = leg_t + tol_f * 2;
ear_x = leg_x + tol_f * 2 + bottom_t * 2;
ear_x_o = bottom_x / 2 - ear_x - ear_x / 2;
ear_y = (ear_leg_po_y + bottom_t) * 2 + bottom_y;

wall_holder_o = wall_t + tol_f * 2;
holder_x = ear_x - bottom_t - wall_holder_o;
holder_x_o = bottom_x / 2 - holder_x / 2 - bottom_t - wall_holder_o;
holder_y_o = bottom_y / 2 - holder_x / 2 - bottom_t - wall_holder_o;

// leg_z = back_y_f / 114 * 180;
// leg_part_z = wall_z + bottom_t * 3;

// top_z = bottom_z - bottom_t;

// lamp_d_f = 76;
// lamp_d2_f =	85;
// lamp_arc_y_f = 24;
// lamp_door_o	= wall_x / 2;
// lamp_bolt_o_f = 2.5;
// lamp_bolt_o2_f = 62;
// lamp_bolt_d_f = 2;
// lamp_bolt_d2_f = 5.5;
// lamp_bolt_z_f = 1.5;


// tube_d = back_y_f / 114 * 40;
// tube_t = bottom_t / 2;
// tube_back_o	= back_y_f / 114 * 40;
// tube_z = back_y_f / 114 * 150;
// tube_x_o = bottom_x / 2 - tube_back_o;
// tube_z_o = bottom_z_o - bottom_t - tube_t;
// tube_internal_d = tube_d - tube_t * 2;
// tube_external_d = tube_internal_d + tube_d / 5;

// front_holes_f = 9;
// front_t = bottom_t / 2;
// front_hole_d = back_y_f / 114 * 8;
// front_hole_segment_y = back_y_f / front_holes_f;
// front_hole_z_o = back_y_f / 114 * 12;

// door_y_o = back_y_f / 114 * 15;
// door_z_o = back_y_f / 114 * 15;
// door_o = back_y_f / 114 * 0.5;
// door_z = wall_z / 114 * 70;

// hinge_y = back_y_f / 114 * 10;
// hinge_z = hinge_y / 10 * 4;
// hinge_d = hinge_y / 10 * 3.2;

// axle_d = hinge_y / 10 * 2.6;
// axle_y_o = door_y_o + door_o / 2;
// door_latch_r1 = axle_d / 2 + 1 + tol_f * 2;
// door_latch_r2 = axle_d / 2 + tol_f * 2;
// lock_y = hinge_d;
// lock_t = lock_y;
// lock_z = back_y_f / 114 * 10;
// lock_t1 = lock_t / 3 * 2;
// lock_t2 = lock_t - lock_t1;
// latch_y = lock_z / 10 * 20;
// latch_axle_o = latch_y / 4;
// latch_r1 = axle_d / 2 + 1;

module cassis() {

    translate([0, 0, - bottom_z_o])
        part_bottom();

    // part_bottom();
    // translate([0, 0, height_of_bottom]) part_top();
    
    translate([0, - left_y_o, 0])
        part_left();

    translate([0, left_y_o, 0])
        part_right();

    translate([-back_x_o, 0, 0])
        part_back();

    // translate([0, 0, height_of_bottom + height_of_sides]) part_front();
}

cassis();