# compatible to Blender 2.77

import bpy
def draw_test():
    for i in range(10):
        bpy.ops.mesh.primitive_cube_add(radius=0.5, location=(i,i,i))

def clean_all_object():
    # Delect objects by type
    for o in bpy.context.scene.objects:
        if o.type == 'MESH':
            o.select = True
        else:
            o.select = False
    # Call the operator only once
    bpy.ops.object.delete()
    # Save and re-open the file to clean up the data blocks
    #bpy.ops.wm.save_as_mainfile(filepath=bpy.data.filepath)
    #bpy.ops.wm.open_mainfile(filepath=bpy.data.filepath)


clean_all_object()
draw_test()
