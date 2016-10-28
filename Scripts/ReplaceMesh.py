import bpy

# the name of the mesh to copy to all selected objects
mesh = bpy.data.meshes["Cube"]

for o in bpy.data.objects:
    if o.select:
        o.data = mesh