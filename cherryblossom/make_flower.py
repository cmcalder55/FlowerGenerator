from os import system
import math
from bpy import data, types, ops, context

    
def reset_scene():
    ''' Print names of objects and scenes already present 
    in workspace and delete them. '''

    # clear interpreter console
    clear = lambda: system('cls')
    clear() 

    # print list of all objects in scene
    for o in context.scene.objects:
        print('\n','Objects in scene: ', o.name,'\n')

    # print list of all scene names
    print(' Scene collection: ',data.scenes.keys(),'\n')
    
    # select all objects currently in the scene and delete
    ops.object.select_all(action='SELECT')
    ops.object.delete(use_global=False)
    print(' Objects deleted.')

def generate_sepal():
    ops.mesh.primitive_cone_add()
    ops.transform.rotate(value = math.radians(180), orient_axis = 'X')
    ops.transform.translate(value=(0.0, 0.0, -1.5)) 

def flower_petals():

#    ops.object.mode_set(mode='OBJECT')

    # make new collection in scene
    petal = data.collections.new('petal')
    context.scene.collection.children.link(petal)

    reset_scene()
    
    ops.object.select_all(action='SELECT')

    # Create a bezier circle and enter edit mode.
    ops.curve.primitive_bezier_circle_add(enter_editmode=True)

    # Randomize the vertices of the bezier circle.
    ops.transform.vertex_random(offset=1.0, uniform=0.1, normal=0.0, seed=0)

    # Scale the curve while in edit mode.
    ops.transform.resize(value=(2.0, 1.5, 2.5))

    # Return to object mode and convert to mesh.
    ops.object.mode_set(mode='OBJECT')
    ops.object.convert(target='MESH', keep_original=False)
    
    # go to edit mode and create face from mesh vertices.
    ops.object.mode_set(mode='EDIT')
    ops.mesh.select_all(action='SELECT')
    ops.mesh.edge_face_add()

    # back to object mode and translate so end of flower will meet the center.
    ops.object.mode_set(mode='OBJECT')
    
    # initial adjustments of first petal
    ops.transform.rotate(value=math.radians(25), orient_axis='Z')    
    ops.transform.translate(value=(0.0, -2.5, 0.0)) 
    
    # connect vertex pairs to shear sides of petals
    ops.object.mode_set(mode='EDIT')
    ops.mesh.select_all(action='DESELECT')
    
    ops.object.mode_set(mode='OBJECT')
    obj = context.active_object
    for i in range(2,11):
        obj.data.vertices[i].select = True

    # connect vertices and dissolve to shape petal edge
    ops.object.mode_set(mode='EDIT')
    ops.mesh.vert_connect()
    ops.mesh.dissolve_verts()
    
    # repeat for other side
    ops.object.mode_set(mode='OBJECT')
    for i in range(6,14):
        obj.data.vertices[i].select = True
        
    ops.object.mode_set(mode='EDIT')
    ops.mesh.vert_connect()
    ops.mesh.dissolve_verts()

    ops.object.mode_set(mode='OBJECT')

    # Rotation * translation for other four petals
    trans_p2 = (2.55, 1.8, 0.0)
    trans_p3 = (-1.0, 3.1, 0.0)
    trans_p4 = (-3.25, -0.17, 0.0)
    trans_p5 = (-0.95, -2.95, 0.0) 

    trans_petal = [trans_p2, trans_p3, trans_p4, trans_p5]

    for i in range(1,5):
        
        if i == 3:
            rot_petal = 80
        else:
            rot_petal = 70
            
        ops.object.duplicate_move()
        ops.transform.rotate(value = -math.radians(rot_petal), orient_axis = 'Z')
        ops.transform.translate(value = trans_petal[i-1]) 

    ops.object.select_all(action = 'SELECT')
    ops.object.move_to_collection(collection_index = 1)

    generate_sepal()

if __name__ == '__main__':
    flower_petals()
