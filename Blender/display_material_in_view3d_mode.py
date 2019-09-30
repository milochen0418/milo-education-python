# You may see this information in your Scripting sceens
#bpy.context.space_data.view_shade = 'MATERIAL'
# But you cannot use it directly because your python console is in different screen area to it
# The way to do it is

import bpy
view3ds = [area.spaces[0] for area in bpy.context.screen.areas if (area.type=="VIEW_3D")]
for view3d in view3ds:
        view3d.viewport_shade='MATERIAL'

