import sys 
from os import system
#import bmesh
import math
#from mathutils import Matrix

from bpy import data, types, ops, context

# clear interpreter console
clear = lambda: system('cls')
clear() 
    
def reset_scene():

    for obj in data.objects:
        print(obj.name)

    # print all scene names in a list
    print(data.scenes.keys())
    
    ops.object.select_all(action='SELECT')
    ops.object.delete(use_global=False)

#    if "Cube" in data.meshes:
#        mesh = data.meshes["Cube"]
#        print("removing mesh", mesh)
#        data.meshes.remove(mesh)

def generate_flower():

    reset_scene()
    
    ops.object.select_all(action='SELECT')

    # # make new collection
    # petal = data.collections.new('petal')
    # context.scene.collection.children.link(petal)

    # Create a bezier circle and enter edit mode.
    ops.curve.primitive_bezier_circle_add(
    # radius=1.0,
    # location=(0.0, 0.0, 0.0),
    # scale=(1.0, 1.0, 1.0),
    enter_editmode=True
    )

    # Randomize the vertices of the bezier circle.
    ops.transform.vertex_random(offset=1.0, uniform=0.1, normal=0.0, seed=0)

    # Scale the curve while in edit mode.
    ops.transform.resize(value=(2.0, 2.0, 3.0))

    # Return to object mode and convert to mesh.
    ops.object.mode_set(mode='OBJECT')
    ops.object.convert(target='MESH', keep_original=False)
    
    
    # go to edit mode and create face from mesh vertices.
    ops.object.mode_set(mode='EDIT')
    ops.mesh.select_all(action='SELECT')
    ops.mesh.edge_face_add()

    # back to object mode and translate so end of flower will meet the center.
    ops.object.mode_set(mode='OBJECT')

    obj = context.active_object

    # Rotation * translation
    ops.transform.rotate(value=math.radians(15), orient_axis='Z')    
    ops.transform.translate(value=(0.3, -3.25, 0.0)) 
    
    ops.object.duplicate_move()
    ops.transform.rotate(value=-math.radians(70), orient_axis='Z')
    ops.transform.translate(value=(2.75, 2.0, 0.0)) 
    
    ops.object.duplicate_move()
    ops.transform.rotate(value=-math.radians(70), orient_axis='Z')
    ops.transform.translate(value=(-1.0, 3.8, 0.0)) 
    
    ops.object.duplicate_move()
    ops.transform.rotate(value=-math.radians(70), orient_axis='Z')
    ops.transform.translate(value=(-4.1, -0.1, 0.0)) 
    
    ops.object.duplicate_move()
    ops.transform.rotate(value=-math.radians(70), orient_axis='Z')
    ops.transform.translate(value=(-1.0, -3.5, 0.0)) 

    # new_obj = src_obj.copy()
    # context.scene.objects.link(new_obj)

if __name__ == '__main__':
    generate_flower()
