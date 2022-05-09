from os import system, path
from bpy import ops, context, data, types, utils

class SimpleOperator(types.Operator):
	# class properties
	bl_idname = "object.petal"
	bl_label = "flower petal"
	
	def execute(self, context):
	
		# print all objects
		for obj in data.objects:
			print(obj.name)

		# print all scene names in a list
		print(data.scenes.keys())

		# remove curves already in workspace
		if "BezierCircle" in data.curves:
		    mesh = data.curves["BezierCircle"]
		    print("removing mesh", mesh)
		    data.curves.remove(mesh)

		# write images into a file next to the blend
		with open(path.splitext(data.filepath)[0] + ".txt", 'w') as fs:
		    for image in data.images:
		        fs.write("%s %d x %d\n" % (image.filepath, image.size[0], image.size[1]))
#		print("Hello World")
		return {'FINISHED'}
	
	
	

# module registration
def register():
	utils.register_class(SimpleOperator)

def unregister():
	utils.unregister_class(SimpleOperator)

# testing execution
if __name__ == "__main__":
	
	# clear interpreter console
	clear = lambda: system('cls')
	clear()
	
	register()



##---graphics start here-----------------------------------------------------------#

## Create a bezier circle and enter edit mode.
#ops.curve.primitive_bezier_circle_add(
#    radius=1.0,
#    location=(0.0, 0.0, 0.0),
#    scale=(1.0, 1.0, 1.0),
#    enter_editmode=True
#)

## Randomize the vertices of the bezier circle.
#ops.transform.vertex_random(offset=1.0, uniform=0.1, normal=0.0, seed=0)

## Scale the curve while in edit mode.
#ops.transform.resize(value=(2.0, 2.0, 3.0))

## Return to object mode.
#ops.object.mode_set(mode='OBJECT')

## Store a shortcut to the curve object's data.
#obj_data = context.active_object.data

### make mesh
##verts = [( 1.0,  1.0,  0.0), 
##         ( 1.0, -1.0,  0.0),
##         (-1.0, -1.0,  0.0),
##         (-1.0,  1.0,  0.0),
##         ]  # 4 verts made with XYZ coords
##edges = []
##faces = [[0, 1, 2, 3]]
##new_mesh = bpy.data.meshes.new('new_mesh')
##new_mesh.from_pydata(verts, edges, faces)
##new_mesh.update()
### make object from mesh
##new_object = bpy.data.objects.new('new_object', new_mesh)
# # make collection
##new_collection = bpy.data.collections.new('new_collection')
##bpy.context.scene.collection.children.link(new_collection)
### add object to scene collection
##new_collection.objects.link(new_object)
