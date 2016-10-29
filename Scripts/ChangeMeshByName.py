import bpy

# the name of the mesh to copy to all selected objects
mesh = bpy.data.meshes["LodA_Railing1x2x.20.blend"]

for o in bpy.data.objects:
    if o.name.startswith("Railing1x2x.20.blend"):
		#o.data = mesh
        print(o.name)
		