import bpy

# current scene
scn = bpy.context.scene

# paths to the blend files
filepaths = ["d:\images\Blender\GameAssets\BlenderSource\BuildingBlocks\LodA\LodA_GlassWall3x4x.2.blend",
		"d:\images\Blender\GameAssets\BlenderSource\BuildingBlocks\LodA\LodA_Wall3x4x.2.blend",
		"d:\images\Blender\GameAssets\BlenderSource\BuildingBlocks\LodA\LodA_WallWithOutLets3x4x.20.blend",
		"d:\images\Blender\GameAssets\BlenderSource\BuildingBlocks\LodA\LodA_WallWithWindow3x4x.20.blend",
		"d:\images\Blender\GameAssets\BlenderSource\BuildingBlocks\LodA\LodA_WallWithDoor3x4x.20.blend",
		"d:\images\Blender\GameAssets\BlenderSource\BuildingBlocks\LodA\LodA_Railing1x2x.20.blend"]

		


# name of object(s) to append or link
obj_name = "LodB_"

# append, set to true to keep the link to the original file
link = True

for filepath in filepaths:
	# link all objects starting with obj_name
	with bpy.data.libraries.load(filepath, link=link) as (data_from, data_to):
		data_to.objects = [name for name in data_from.objects if name.startswith(obj_name)]

	#link object to current scene
	for obj in data_to.objects:
		if obj is not None:
		   scn.objects.link(obj)
