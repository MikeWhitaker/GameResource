import bpy

filepath = "/path/to/file.blend"
group_name = "CubeGroup"
# append, set to true to keep the link to the original file
link = False 

# append all groups from the .blend file
with bpy.data.libraries.load(filepath, link=link) as (data_src, data_dst):
    ## all groups
    # data_to.groups = data_from.groups

    # only append a single group we already know the name of
    data_dst.groups = [group_name]

# add the group instance to the scene
scene = bpy.context.scene
for group in data_dst.groups:
    ob = bpy.data.objects.new(group.name, None)
    ob.dupli_group = group
    ob.dupli_type = 'GROUP'
    scene.objects.link(ob)