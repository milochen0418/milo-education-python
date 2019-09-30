import bpy
view3ds = [area.spaces[0] for area in bpy.context.screen.areas if (area.type=="VIEW_3D")]
for view3d in view3ds:
    view3d.pivot_point='CURSOR'
    view3d.cursor_location = (0.0, 0.0, 0.0)

