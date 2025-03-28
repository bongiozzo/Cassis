
# %%
from ocp_vscode import show, set_port, show_clear, show_all
from build123d import *
from config import *
from parts import *

# Necessary to Debug Cell in Notebook 
set_port(3939)
# Clear the scene
show_clear()

# Create parts
part_bottom = create_bottom()
part_top = create_top()
part_back = create_back()
part_left = create_left()
part_right = create_right()
part_tube = create_tube()
part_leg = Pos(-EAR_X_O-LEG_X/2,-BOTTOM_Y/2-BOTTOM_T, -LEG_PART_Z) * Rot(0,90, 90) * create_leg()
# And assembly
assembly_front = create_front_assembly()

# Show all parts in Viewport with ability to filter needed
show_all()

# Export for printing
export_stl(part_bottom,"bottom.stl")
export_stl(part_top,"top.stl")
export_stl(part_back,"back.stl")
export_stl(part_left,"left.stl")
export_stl(part_right,"right.stl")
export_stl(part_tube,"tube.stl")
export_stl(part_leg,"leg.stl")
export_stl(assembly_front,"front.stl")
# %%
