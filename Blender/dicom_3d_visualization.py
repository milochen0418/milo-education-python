import bpy

def removeAllObjs():
    # remove all elements in scene
    bpy.ops.object.select_by_layer()
    bpy.ops.object.delete(use_global=False)

def setAll3DCursorsZeros():
    # set 3d cursors to zeros 
    view3ds = [area.spaces[0] for area in bpy.context.screen.areas if (area.type=="VIEW_3D")]
    for view3d in view3ds:
        view3d.pivot_point='CURSOR'
        view3d.cursor_location = (0.0, 0.0, 0.0)
def setMaterialModeInView3D():
    # set to material mdoe in view3d
    view3ds = [area.spaces[0] for area in bpy.context.screen.areas if (area.type=="VIEW_3D")]
    for view3d in view3ds:
        view3d.viewport_shade='MATERIAL'

def enableImportImageAsPlane():
    # Set user preference to support import images as plane 
    bpy.ops.wm.addon_enable(module='io_import_images_as_planes')
def add_image_plane(image_filepath, alpha=0.3, location=(0,0,0)):
    bpy.ops.import_image.to_plane(location=(0,0,0), files=[{"name":image_filepath}])
    obj = bpy.context.object # or bpy.data.objects['CT']
    obj.active_material.emit = 1
    obj.active_material.diffuse_intensity = 0 
    obj.active_material.specular_intensity = 0
    obj.active_material.use_transparency = True
    obj.active_material.alpha = 0.3     
    return obj

def init_env():
    # remove all elements in scene
    removeAllObjs()
    # set 3d cursors to zeros 
    setAll3DCursorsZeros()
    # set to material mdoe in view3d
    setMaterialModeInView3D()
    # Set user preference to support import images as plane 
    enableImportImageAsPlane()

    # Set test image_filepath
    image_filepath = '/Users/milochen/Desktop/CT.png'
    obj = add_image_plane(image_filepath)


init_env()
