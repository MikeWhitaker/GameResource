import bpy
import mathutils

print("Start run ...")

vec = mathutils.Vector((0.0, 0.0, 0.0))

for obj in bpy.context.selected_objects:
#    for coord in obj.matrix_world.to_translation():
#        print(coord.x)

    
    #print(round(obj.matrix_world.to_translation().x,1))
    print(obj.location.x)
    vec.x = round(obj.location.x,1)
    vec.y = round(obj.location.y,1)
    vec.z = round(obj.location.z,1)
    print(vec)
    obj.location = vec
    
    print("After Operation:")
    print(obj.location.x)
    
