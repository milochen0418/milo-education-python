# compatible to Blender 2.77

import bpy
def draw_test():
    for i in range(10):
        bpy.ops.mesh.primitive_cube_add(radius=0.5, location=(i,i,i))
def draw_plane_test():
    bpy.ops.mesh.primitive_plane_add(radius=2, location=(0,0,0))
    
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
    
def draw_point(pt):
    (x,y,z) = tuple(pt)
    bpy.ops.mesh.primitive_cube_add(radius=0.1, location=(1.0*x,1.0*y,1.0*z))

def test_case_draw_point():    
    for i in range(10):
        pt = [i,i,i]
        draw_point(pt)

    
clean_all_object()
#draw_test()
test_case_draw_point()
draw_plane_test()