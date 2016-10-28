import bpy

# current scene
scn = bpy.context.scene

# path to the blend
filepath = "d:\\images\\Blender\\test\\linkImport\\LodA_WallWithDoor3x4x.20.blend"

# name of object(s) to append or link
obj_name = "LodA_WallWithDoor3x4x.20"

# append, set to true to keep the link to the original file
link = True

# link all objects starting with 'Cube'
with bpy.data.libraries.load(filepath, link=link) as (data_from, data_to):
    data_to.objects = [name for name in data_from.objects if name.startswith(obj_name)]

#link object to current scene
for obj in data_to.objects:
    if obj is not None:
       scn.objects.link(obj)