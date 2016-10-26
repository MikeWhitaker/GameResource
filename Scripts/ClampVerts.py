import bpy, bmesh, mathutils

obj = bpy.context.active_object

if obj.mode == 'EDIT':
	
	selected_verts = list(filter(lambda v: v.select, obj.vertices))
	for vert in fselected_verts:
			print(vert.Vertex.x)
			print(vert.Vertex.y)
			print(vert.Vertex.z)

else:
    #vertices = obj.data.vertices
	print("Not in Edit mode ...")
	exit()

#verts = [obj.matrix_world * vert.co for vert in vertices] 

# coordinates as tuples
#plain_verts = [vert.to_tuple() for vert in verts]
#print(plain_verts)