include <BOSL2/joints.scad>

module door_assembly() {
    // Frame with predefined hinge anchors
    frame() {
        cuboid([200,20,300], anchor=BOTTOM);
        attach(TOP, HINGE_LEFT) {};  // Hinge anchor point
    }

    // Door constrained to hinge axis
    attach(frame, HINGE_LEFT, UP) {
        rotate(ang, from=HINGE_AXIS)
            cuboid([190,15,290], anchor=BOTTOM);
    }
    
    // Check door-frame clearance
    assert(door_width < frame_width-2*slop, "Door too wide!");
}

door() {
    attach(HINGE_LEFT, box_front())  // Anchor door hinge to front panel
        rotate([0, hinge_angle, 0])
            cuboid([door_width, door_thickness, door_height]);
}

// Hinge joint between door and frame
hinge_joint(
    part1 = door,
    part2 = frame,
    axis = LEFT,
    angle_limit = [0, 90]  // Constrain door to 90° swing
);

// Verify door doesn't intersect frame when open
door_sweep = rot(ang, from=HINGE_AXIS) * door_profile;
if (len(intersection(door_sweep, frame_profile)) > 0) {
    echo("Collision detected at angle ", ang);
}