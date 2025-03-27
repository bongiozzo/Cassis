from math import sqrt
from build123d import *
from config import *

def create_base(base_height) -> Part:

    sk_ear = Rectangle(EAR_X, EAR_Y)
    sk_ear -= offset(sk_ear, -BOTTOM_T)
    ears = Pos(-EAR_X_O,0) * sk_ear + Pos(EAR_X_O,0) * sk_ear
    sk_base = Rectangle(BOTTOM_X, BOTTOM_Y)
    part_base = extrude(sk_base + ears, base_height)
    part_base -= extrude(Plane(part_base.faces().sort_by()[-1]) * offset(sk_base, -BOTTOM_T), -(base_height-BOTTOM_T))

    #! Replace with flipped parts?
    sk_holders = Pos(-HOLDER_X_O,HOLDER_Y_O) * Rectangle(HOLDER_X, BOTTOM_T, align=(Align.MIN, Align.MAX)) + \
                 Pos(-HOLDER_X_O,HOLDER_Y_O) * Rectangle(BOTTOM_T, HOLDER_X, align=(Align.MIN, Align.MAX)) + \
                 Pos(HOLDER_X_O,HOLDER_Y_O) * Rectangle(HOLDER_X, BOTTOM_T, align=(Align.MAX, Align.MAX)) + \
                 Pos(HOLDER_X_O,HOLDER_Y_O) * Rectangle(BOTTOM_T, HOLDER_X, align=(Align.MAX, Align.MAX)) + \
                 Pos(HOLDER_X_O,-HOLDER_Y_O) * Rectangle(HOLDER_X, BOTTOM_T, align=(Align.MAX, Align.MIN)) + \
                 Pos(HOLDER_X_O,-HOLDER_Y_O) * Rectangle(BOTTOM_T, HOLDER_X, align=(Align.MAX, Align.MIN)) + \
                 Pos(-HOLDER_X_O,-HOLDER_Y_O) * Rectangle(HOLDER_X, BOTTOM_T, align=(Align.MIN, Align.MIN)) + \
                 Pos(-HOLDER_X_O,-HOLDER_Y_O) * Rectangle(BOTTOM_T, HOLDER_X, align=(Align.MIN, Align.MIN))

    sk_holders += Pos(EAR_X_O, HOLDER_Y_O) * Rectangle(LEG_X, BOTTOM_T, align=(Align.CENTER, Align.MAX)) + \
                  Pos(EAR_X_O, -HOLDER_Y_O) * Rectangle(LEG_X, BOTTOM_T, align=(Align.CENTER, Align.MIN)) 

    part_base += extrude(sk_holders, base_height)

    return part_base

def create_bottom() -> Part:

    part_bottom = create_base(BOTTOM_Z)

    bolts_arc_center_x = BOTTOM_X/2-LAMP_DOOR_O
    bolts_arc_r = LAMP_D_F/2+LAMP_BOLT_O_F
    bolt1_y = LAMP_BOLT_O2_F/2
    bolt1_x = sqrt(bolts_arc_r**2 - bolt1_y**2)

    holes = Locations((-bolts_arc_r,0),(bolt1_x, bolt1_y),(bolt1_x, -bolt1_y))
    sk_bolts1 = Sketch() + [loc * Circle(LAMP_BOLT_D2_F/2*2) for loc in holes]
    sk_bolts2 = Sketch() + [loc * Circle(LAMP_BOLT_D2_F/2) for loc in holes]
    part_bottom += extrude(sk_bolts1, BOTTOM_Z)
    part_bottom -= extrude(sk_bolts2, LAMP_BOLT_Z_F)
    sk_holes = Sketch() + Pos(bolts_arc_center_x, 0) * Circle(LAMP_D_F/2) + [loc * Circle(LAMP_BOLT_D_F/2) for loc in holes]
    part_bottom -= extrude(sk_holes, BOTTOM_Z)

    second_arc_x = LAMP_ARC_Y_F / 2
    second_arc_r = LAMP_D2_F / 2
    second_arc_y = sqrt(second_arc_r**2 - second_arc_x**2)

    l1 = Line((-second_arc_x, 0), (-second_arc_x, second_arc_y))
    l2 = Line((second_arc_x, second_arc_y), (second_arc_x, 0))
    l_arc = ThreePointArc((l1 @ 1, (0, second_arc_r), l2 @ 0))
    ln = Curve() + [l1, l_arc, l2]
    ln += mirror(ln, Plane.XZ)
    sk_holes = make_face(ln)
    part_bottom -= extrude(sk_holes, BOTTOM_Z)

    part_bottom.label = "Bottom"
    return Pos(0,0,-BOTTOM_Z_O) * part_bottom

def create_top() -> Part:

    part_top = create_base(TOP_Z)

    sk_hole = Pos(-(BOTTOM_X/2-TUBE_BACK_O),0) * Circle(TUBE_D/2)
    part_top -= extrude(sk_hole , TOP_Z)

    #! FIx orientation?
    part_top.label = "Top"
    return Pos(0,0,BOTTOM_Z_O) * Rot(180, 0, 0) * part_top

def create_back() -> Part:

    wall = Plane.YZ * Box(BACK_Y_F, WALL_Z, WALL_T)

    wall.label = "Back"
    return Pos(-BACK_X_O, 0, 0) * wall

def create_left() -> Part:

    wall = Plane.XZ * Box(WALL_X, WALL_Z, WALL_T)

    wall.label = "Left"
    return Pos(0, -LEFT_Y_O, 0) * wall

def create_right() -> Part:

    wall = Plane.XZ * Box(WALL_X, WALL_Z, WALL_T)

    wall.label = "Right"
    return Pos(0, LEFT_Y_O, 0) * wall

def create_tube() -> Part:

    part_tube = extrude(Circle(TUBE_EXTERNAL_D/2) - Circle(TUBE_INTERNAL_D/2), TUBE_T)
    part_tube += extrude(Circle(TUBE_D/2) - Circle(TUBE_INTERNAL_D/2), TUBE_Z)

    part_tube.label = "Tube"
    return Pos(-TUBE_X_O,0,TUBE_Z_O) * part_tube

def create_leg() -> Part:

    l1 = Line((0, 0), (0, LEG_Z))
    l2 = Line(l1 @ 1, (LEG_T, LEG_Z))
    l3 = Line(l2 @ 1, (LEG_T, LEG_Z-LEG_PART_Z))
    l4 = Line(l3 @ 1, (LEG_T*2, (l3 @ 1).Y))
    l5 = Line(l4 @ 1, (LEG_T, (l4 @ 1).Y-LEG_T))
    l6 = Line(l5 @ 1, (LEG_T, LEG_T))
    l7 = Line(l6 @ 1, (LEG_T*2, 0))
    l8 = Line(l7 @ 1, l1 @ 0)
    ln = Curve() + [l1, l2, l3, l4, l5, l6, l7, l8]
    sk_leg = make_face(ln)
    part_leg = extrude(sk_leg, LEG_X)
    part_leg = fillet(part_leg.edges(),LEG_FILLET)
    
    part_leg.label = "Leg"
    return part_leg

def create_front_assembly() -> Compound:

    sk_front = Rectangle(BACK_Y_F, WALL_Z) - Pos(-(BACK_Y_F/2-DOOR_Y_O), WALL_Z/2-DOOR_Z_O) * Rectangle(FRONT_DOOR_X, FRONT_DOOR_Z, align=(Align.MIN, Align.MAX))

    holes = Sketch() + [
        loc * Pos(Y=-WALL_Z/2+FRONT_HOLE_Z_O) * Circle(FRONT_HOLE_D/2)
        for loc in GridLocations(BACK_Y_F / FRONT_HOLES_F, 0, FRONT_HOLES_F, 1)
    ]
    sk_front -= holes
    part_front = extrude(sk_front, FRONT_T)

    plane_door = Plane.XY * Pos(0, FRONT_DOOR_CENTER_Z_O, FRONT_T)

    sk_lock = plane_door * Pos(FRONT_DOOR_X/2, -LOCK_Z/2+LOCK_X) * Rectangle(LOCK_X, LOCK_X, align=(Align.MIN, Align.MAX))
    part_front += extrude(sk_lock, LOCK_T1)
    sk_lock = plane_door * Pos(FRONT_DOOR_X/2, 0, LOCK_T1) * Rectangle(LOCK_X, LOCK_Z, align=(Align.MIN, Align.CENTER))
    part_front += extrude(sk_lock, LOCK_T2)

    # Reorient?
    plane_hinge = Plane.XZ * Pos(-FRONT_DOOR_X/2+DOOR_O/2, FRONT_T, -FRONT_DOOR_Z/2-FRONT_DOOR_CENTER_Z_O)

    sk_hinge = plane_hinge * split(Circle(HINGE_Y/2), keep=Keep.BOTTOM)
    sk_hinge -= plane_hinge * Pos(Y=HINGE_CENTER_Y_O) * Circle(HINGE_D/2)
    part_hinge = extrude(sk_hinge, -HINGE_Z)
    part_hinge += mirror(part_hinge, about=Plane.XZ.offset(-FRONT_DOOR_CENTER_Z_O))
    part_front += part_hinge

    sk_door = plane_door * Rectangle(FRONT_DOOR_X - DOOR_O*2, DOOR_Z)
    part_door = extrude(sk_door, -FRONT_T)

    plane_hinge = plane_hinge.offset(DOOR_O)
    sk_door = plane_hinge * split(Circle(HINGE_Y/2), keep=Keep.BOTTOM)
    sk_door = split(sk_door, bisect_by=Plane.YZ.offset(-FRONT_DOOR_X/2+DOOR_O/2))
    sk_door += plane_hinge * Pos(Y=HINGE_CENTER_Y_O) * Circle(HINGE_Y/4-DOOR_O/2)
    part_hinge = extrude(sk_door, HINGE_Z)
    sk_axle = plane_hinge * Pos(Y=HINGE_CENTER_Y_O) * Circle(AXLE_D/2)
    part_hinge += extrude(sk_axle, -(HINGE_Z+DOOR_O))
    part_hinge += mirror(part_hinge, about=Plane.XZ.offset(-FRONT_DOOR_CENTER_Z_O))
    part_door += part_hinge

    latch_center = Pos(FRONT_DOOR_X/2-LATCH_AXLE_O, FRONT_DOOR_CENTER_Z_O, 0)

    part_door -= latch_center * Cone(DOOR_LATCH_R1, DOOR_LATCH_R2, FRONT_T+DOOR_O, align=(Align.CENTER, Align.CENTER, Align.MIN))

    part_latch = latch_center * Cone(LATCH_R1, AXLE_D/2, FRONT_T+DOOR_O, align=(Align.CENTER, Align.CENTER, Align.MIN))
    part_latch += Pos(FRONT_DOOR_X/2-LATCH_AXLE_O*2, FRONT_DOOR_CENTER_Z_O, FRONT_T+DOOR_O) * Box(LATCH_Y, LOCK_X, FRONT_T, align=(Align.MIN, Align.CENTER, Align.MIN))
    part_latch += Pos(FRONT_DOOR_X/2-LATCH_AXLE_O*2+LATCH_Y-LOCK_X, FRONT_DOOR_CENTER_Z_O, FRONT_T+DOOR_O) * Box(LOCK_X, LOCK_X, LOCK_T, align=(Align.MIN, Align.CENTER, Align.MIN))

    front = Compound(label="Front", children=[part_front, part_door, part_latch])

    #! Why Y and not Z were rotated? ) 
    return Pos(BACK_X_O-FRONT_T/2,0,0) * Rot(90, 90, 0) * front
