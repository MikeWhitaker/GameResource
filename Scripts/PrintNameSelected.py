import bpy

#show the name of the selected object

for o in bpy.data.objects:
    if o.select:
        #o.data = mesh
        print(o.name)
        print(o.data)
		