import bpy

# the name of the mesh to copy to all selected objects
mesh = bpy.data.meshes["LodB_WallWithDoor3x4x.20"]

for o in bpy.data.objects:
    if o.select:
        o.data = mesh
		