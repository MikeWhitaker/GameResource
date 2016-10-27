import bpy
import mathutils

print("Start run ...")

vec = mathutils.Vector((0.0, 0.0, 0.0))

for obj in bpy.context.selected_objects:
#    for coord in obj.matrix_world.to_translation():
#        print(coord.x)

    
    #print(round(obj.matrix_world.to_translation().x,1))
    obj.location = vec
    
    print("After Operation:")
    print(obj.location.x)
    