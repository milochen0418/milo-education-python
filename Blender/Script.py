# compatible to Blender 2.77

import bpy
def draw_test():
    for i in range(10):
        bpy.ops.mesh.primitive_cube_add(radius=0.5, location=(i,i,i))
def draw_plane_test():
    bpy.ops.mesh.primitive_plane_add(radius=2, location=(0,0,0))
 
def removeAll(type=None):
    # Possible type: ‘MESH’, ‘CURVE’, ‘SURFACE’, ‘META’, ‘FONT’, ‘ARMATURE’,
‘LATTICE’, ‘EMPTY’, ‘CAMERA’, ‘LAMP’
    if type:
        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.select_by_type(type=type)
        bpy.ops.object.delete()
    else:
        # Remove all elements in scene
        bpy.ops.object.select_by_layer()
        bpy.ops.object.delete(use_global=False)   
def clean_all_object():
    removeAll()  
def draw_point(pt):
    (x,y,z) = tuple(pt)
    bpy.ops.mesh.primitive_cube_add(radius=0.1, location=(1.0*x,1.0*y,1.0*z))

def test_case_draw_point():    
    for i in range(10):
        pt = [i,i,i]
        draw_point(pt)

    
clean_all_object()
#draw_test()
#test_case_draw_point()
#draw_plane_test()
