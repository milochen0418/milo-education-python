import bpy
for idx,area in enumerate(bpy.context.screen.areas):
    print("idx={} -> {}".format(idx, area.type))

