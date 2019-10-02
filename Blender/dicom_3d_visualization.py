import bpy


def removeAllObjs():
    # remove all elements in scene
    bpy.ops.object.select_by_layer()
    bpy.ops.object.delete(use_global=False)
    # Clean all materials 
    for material in bpy.data.materials:
        if not material.users:
            bpy.data.materials.remove(material)    

def removeAllObjsWithoutCamera():
    #types = ['MESH', 'CURVE', 'SURFACE', 'META', 'FONT', 'ARMATURE', 'LATTICE', 'EMPTY', 'CAMERA', 'LAMP', 'SPEAKER']
    types = ['MESH', 'CURVE', 'SURFACE', 'META', 'FONT', 'ARMATURE', 'LATTICE', 'EMPTY', 'CAMERA', 'LAMP', 'SPEAKER']
    # All types is refer to document of https://docs.blender.org/api/blender_python_api_current/bpy.ops.object.html
    types.remove('CAMERA')
    for item in types:
        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.select_by_type(type=item)
        bpy.ops.object.delete()        
        
    

def setAll3DCursorsZeros():
    # set 3d cursors to zeros 
    view3ds = [area.spaces[0] for area in bpy.context.screen.areas if (area.type=="VIEW_3D")]
    for view3d in view3ds:
        view3d.pivot_point='CURSOR'
        view3d.cursor_location = (0.0, 0.0, 0.0)
        
def set3DCursorsXYZ(x,y,z):
    view3ds = [area.spaces[0] for area in bpy.context.screen.areas if (area.type=="VIEW_3D")]
    for view3d in view3ds:
        view3d.pivot_point='CURSOR'
        view3d.cursor_location = (x, y, z)
    
def setMaterialModeInView3D():
    # set to material mdoe in view3d
    view3ds = [area.spaces[0] for area in bpy.context.screen.areas if (area.type=="VIEW_3D")]
    for view3d in view3ds:
        view3d.viewport_shade='MATERIAL'
def setCamera(): 
    
    pass

def enableImportImageAsPlane():
    # Set user preference to support import images as plane 
    bpy.ops.wm.addon_enable(module='io_import_images_as_planes')
def add_image_plane(image_filepath, alpha=0.3, location=(0,0,0)):
    #bpy.ops.import_image.to_plane(location=(0,0,0), files=[{"name":image_filepath}])
    bpy.ops.import_image.to_plane(location=location, files=[{"name":image_filepath}])
    obj = bpy.context.object # or bpy.data.objects['CT']
    obj.active_material.emit = 2
    obj.active_material.diffuse_intensity = 0 
    obj.active_material.specular_intensity = 0
    obj.active_material.use_transparency = True
    obj.active_material.alpha = alpha
    obj.show_transparent = True
    #obj.show_wire = True
    obj.show_wire = False
    #obj.active_material.transparency_method = 'MASK_Z' # MASK Z_TRANSPARENCY
    #obj.active_material.transparency_method = 'Z_TRANSPARENCY'
    obj.dimensions = (2, 2, 0.0)
    # Set dimensions for fit dicom image pixel_array ( 512x512 pixel)
    
    return obj
def draw_point(pt):
    (x,y,z) = tuple(pt)
    bpy.ops.mesh.primitive_cube_add(radius=0.02, location=(0.5*x,0.5*y,0.5*z))


def add_text(radius = 0.3, location=(0,0,0), text='Hello', color=(2.0,0,0)):
    bpy.ops.object.text_add(radius = radius, location = location)
    obj = bpy.context.object
    mesh = bpy.context.object.data
    
    obj.data.body = text
        
    mat_red = bpy.data.materials.new("Text")
    #mat_red.diffuse_color = (2.0, 0.0, 0.0)
    mat_red.diffuse_color = color
    mat_red.emit = 2
    
    if len(mesh.materials) == 0:
        mesh.materials.append(mat_red)
    else:
        mesh.materials[0] = mat_red    
    return obj

def init_color_material():
    bpy.data.materials.new(name="Color_R")
    mat = bpy.data.materials.get("Color_R")
    mat.diffuse_color = (2,0,0)
    mat.emit(2)
    
    bpy.data.materials.new(name="Color_G")
    mat = bpy.data.materials.get("Color_G")
    mat.diffuse_color = (0,1,0)
    
    bpy.data.materials.new(name="Color_B")
    mat = bpy.data.materials.get("Color_B")
    mat.diffuse_color = (0,0,1)
    

def init_env():
    # init basic color material
    
    # remove all elements in scene
    # removeAllObjs()
    
    # remove all elements in scene but not Camera
    removeAllObjsWithoutCamera()
    #return 
    
    # set 3d cursors to zeros 
    setAll3DCursorsZeros()
    # set to material mdoe in view3d
    setMaterialModeInView3D()
    # Set user preference to support import images as plane 
    enableImportImageAsPlane()

    # Set test images
    image_filepath = '/Users/milochen/Desktop/CT.png'
    for slice_idx in range(20):
        set3DCursorsXYZ(0.0, 0.0, 0.2 * slice_idx)
        obj = add_image_plane(image_filepath)
        pass

    text_obj = add_text(text='3D CT data show', radius=0.3 , location=(1,1,0),color=(2,0,0))
    text_obj2 = add_text(text='3D3D', radius=0.3 , location=(1,1,0.5), color=(2,0,0))

    for i in range(10):
        pt = [0,0,i]
        draw_point(pt)


init_env()


