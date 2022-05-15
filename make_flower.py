
from os import system
import math
from mathutils import Euler
from bpy import data, ops, context
  
def reset_scene():
    ''' Print names of objects and scenes already present in 
    workspace and delete them. '''

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

    # check if petal collection exists, add and link to scene if needed
    name = 'petal'
    # col = data.collections
    col = data.collections.new(name)
    context.scene.collection.children.link(col)

    # for o in data.collections:
    #     if o.name == name:
    #         print('Collection found.')
    #     else:
    #         col = data.collections.new(name)
    #         context.scene.collection.children.link(col)
    #         print('Collection created.')

def generate_stamen_base():
    '''Generate base to connect stamen to the stem.'''
    ops.object.mode_set(mode='OBJECT')
    # add cone for receptacle
    ops.mesh.primitive_cone_add(rotation=(0,math.pi,0))
    # scale and rotate
    # ops.transform.rotate(value = math.radians(180), orient_axis = 'X')
    cone_scale = 0.629
    base_scale = (cone_scale, cone_scale, cone_scale)
    ops.transform.resize(value=base_scale)
    # translate to align with petals
    cone_trans = (0.02, 0.09, -1.22)
    ops.transform.translate(value=cone_trans) 
    # add torus for top of the stamen base and scale
    ops.mesh.primitive_torus_add(major_radius=0.93,minor_radius=.12)
    # torus_scale = 0.918
    # top_scale = (torus_scale, torus_scale, torus_scale)
    top_scale = base_scale
    ops.transform.resize(value=top_scale)
    torus_trans = (0.02, 0.09, -0.55)
    ops.transform.translate(value=torus_trans)
    context.active_object.name = 'basecap'
    ops.mesh.primitive_uv_sphere_add(location=(0.02,0.09,-1.4))
    # points to keep 
    points = [0, 1, 2]
    keep = []
    ob = points

    for i in range(32):
        if i == 0:
            keep.extend(points)
        else:
            if i == 1:
                extend = 10
            elif i == 22:
                extend = 16
            else: 
                extend = 15
            ob = list(map(lambda x: x+extend, ob))
            keep.extend(ob)
    keep.append(325)

    obj = context.active_object
    ops.object.mode_set(mode='EDIT')
    ops.mesh.select_mode(type='VERT')
    ops.mesh.select_all(action='DESELECT')
    ops.object.mode_set(mode='OBJECT')
    
    for i in range(482):
        if i not in keep:
            obj.data.vertices[i].select = True

    ops.object.mode_set(mode='EDIT')
    ops.mesh.dissolve_verts()
    
    name = 'stamen base'
    col = data.collections.new(name)
    context.scene.collection.children.link(col)
    
    generate_stamen()
    # ops.object.mode_set(mode='EDIT')

def generate_stamen():
    '''Generate stamens from the middle of the flower.'''
    n_stamen = 10
    name = 'stamen'
    col = data.collections.new(name)
    context.scene.collection.children.link(col)
    # generate nurbs curve and bezier circle
    ops.curve.primitive_nurbs_curve_add()
    stamen_curve = context.active_object.data.name
    ops.curve.primitive_bezier_circle_add(radius=0.02)
    # apply circle as cross section for cylinder
    x_section = context.active_object
    curve_data = data.curves[stamen_curve]
    curve_data.bevel_mode = 'OBJECT'
    curve_data.bevel_object = x_section
    # convert curve to mesh
    obj1 = data.objects['NurbsCurve']
    obj1.select_set(True)    
    context.view_layer.objects.active = obj1
    ops.object.convert(target='MESH')
    # generate stamen tip and join with beveled curve
    ops.mesh.primitive_uv_sphere_add(radius=0.05)
    ops.transform.translate(value=(-0.75,0.83,0.0))
    rot_tip = (-23.5, 91, 1.4)
    rot_tip = list(map(lambda x: math.radians(x), rot_tip))
    stamen1 = data.objects['Sphere.001']
    stamen1.rotation_euler = Euler((rot_tip), 'XYZ')
    
    obj1.select_set(True)
    # consider "bridge edge"
    ops.object.join()
    ops.transform.resize(value=(2.0, 2.0, 2.0))
    
    stamen1.name = 'stamen1'
    rot1 = (-59, 186, -2.01)
    trans1 = (0.04, -1.94, 1.81)
    rot = list(map(lambda x: math.radians(x), rot1))
    stamen1.rotation_euler = Euler((rot), 'XYZ')
    stamen1.location.xyz = trans1
    ops.object.move_to_collection(collection_index = 3)

    for i in range(2,n_stamen+1):
        ops.object.duplicate()
        obj_name = 'stamen'+str(i)
        context.active_object.name = obj_name

    stamen2 = data.objects['stamen2']
    rot2 = (-52.6, 180, 33.3)
    trans2 = (0.9,-1.45,2.04)
    rot = list(map(lambda x: math.radians(x), rot2))
    stamen2.rotation_euler = Euler((rot), 'XYZ')
    stamen2.location.xyz = trans2

    stamen3 = data.objects['stamen3']
    rot3 = (-59,186,54.2)
    trans3 = (1.63,-0.84,1.81)
    rot = list(map(lambda x: math.radians(x), rot3))
    stamen3.rotation_euler = Euler((rot), 'XYZ')
    stamen3.location.xyz = trans3

    stamen4 = data.objects['stamen4']
    rot4 = (-33.3,186,103)
    trans4 = (0.45,0.52,2.27)
    rot = list(map(lambda x: math.radians(x), rot4))
    stamen4.rotation_euler = Euler((rot), 'XYZ')
    stamen4.location.xyz = trans4

    stamen5 = data.objects['stamen5']   
    rot5 = (-57.7,178,-84.2)
    trans5 = (-1.88,0.06,1.91)
    rot = list(map(lambda x: math.radians(x), rot5))
    stamen5.rotation_euler = Euler((rot), 'XYZ')
    stamen5.location.xyz = trans5

    stamen6 = data.objects['stamen6']
    rot6 = (126,0,62.6)
    trans6 = (-1.52,1.08,1.76)
    rot = list(map(lambda x: math.radians(x), rot6))
    stamen6.rotation_euler = Euler((rot), 'XYZ')
    stamen6.location.xyz = trans6

    stamen7 = data.objects['stamen7']
    rot7 = (124,-6,-6.81)
    trans7 = (-0.01,2.02,1.88)
    rot = list(map(lambda x: math.radians(x), rot7))
    stamen7.rotation_euler = Euler((rot), 'XYZ')
    stamen7.location.xyz = trans7

    stamen8 = data.objects['stamen8']
    rot8 = (1-59,186,-47.7)
    trans8 = (-1.27,-1.41,1.81)
    rot = list(map(lambda x: math.radians(x), rot8))
    stamen8.rotation_euler = Euler((rot), 'XYZ')
    stamen8.location.xyz = trans8

    stamen9 = data.objects['stamen9']
    rot9 = (122,11.9,-7.91)
    trans9 = (0.94,1.92,1.73)
    rot = list(map(lambda x: math.radians(x), rot9))
    stamen9.rotation_euler = Euler((rot), 'XYZ')
    stamen9.location.xyz = trans9

    stamen10 = data.objects['stamen10']
    rot10 = (-59,186,89.8)
    trans10 = (2.02,0.3,1.81)
    rot = list(map(lambda x: math.radians(x), rot10))
    stamen10.rotation_euler = Euler((rot), 'XYZ')
    stamen10.location.xyz = trans10

    add_color()

def add_color():
    '''Generate sepal; leaves on the stem on underside of the petals.'''
    # flower petals
    obj = data.objects['BezierCircle']
    obj.color = (0.857,0.594,1,1)
    # Create a material
    mat = data.materials.new('pink')
    # Activate its nodes and assign color
    mat.use_nodes = True
    mat.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value = (0,0,1,1)
    # Assign the material to the object
    obj.data.materials.append(mat)
    
    obj = data.objects['BezierCircle.001']
    obj.color = (0.857,0.594,1,1)
    mat = data.materials.new('pink')
    mat.use_nodes = True
    mat.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value = (0,0,1,1)
    obj.data.materials.append(mat)
    
    obj = data.objects['BezierCircle.002']
    obj.color = (0.857,0.594,1,1)
    mat = data.materials.new('pink')
    mat.use_nodes = True
    mat.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value = (0,0,1,1)
    obj.data.materials.append(mat)
    
    obj = data.objects['BezierCircle.003']
    obj.color = (0.857,0.594,1,1)
    mat = data.materials.new('pink')
    mat.use_nodes = True
    mat.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value = (0,0,1,1)
    obj.data.materials.append(mat)
    
    obj = data.objects['BezierCircle.004']
    obj.color = (0.857,0.594,1,1)
    mat = data.materials.new('pink')
    mat.use_nodes = True
    mat.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value = (0,0,1,1)
    obj.data.materials.append(mat)
    
    # stamen base
    obj = data.objects['Cone']
    obj.color = (.156,.384,.062,1)
    mat = data.materials.new('green')
    mat.use_nodes = True
    mat.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value = (0,0,1,1)
    obj.data.materials.append(mat)
    
    obj = data.objects['Sphere']
    obj.color = (0.384,0.011,0.1,1)
    mat = data.materials.new('maroon')
    mat.use_nodes = True
    mat.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value = (0,0,1,1)
    obj.data.materials.append(mat)
    
    obj = data.objects['basecap']
    obj.color = (0.384,0.011,0.1,1)
    mat = data.materials.new('maroon')
    mat.use_nodes = True
    mat.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value = (0,0,1,1)
    obj.data.materials.append(mat)
    
    # stamen
    obj = data.objects['stamen1']
    obj.color = (0.814,0.396,0.536,1)
    mat = data.materials.new("pink-white")
    mat.use_nodes = True
    mat.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value = (0,0,1,1)
    obj.data.materials.append(mat)
    
    obj = data.objects['stamen2']
    obj.color = (0.814,0.396,0.536,1)
    mat = data.materials.new("pink-white")
    mat.use_nodes = True
    mat.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value = (0,0,1,1)
    obj.data.materials.append(mat)
    
    obj = data.objects['stamen3']
    obj.color = (0.814,0.396,0.536,1)
    mat = data.materials.new("pink-white")
    mat.use_nodes = True
    mat.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value = (0,0,1,1)
    obj.data.materials.append(mat)
    
    obj = data.objects['stamen4']
    obj.color = (0.814,0.396,0.536,1)
    mat = data.materials.new("pink-white")
    mat.use_nodes = True
    mat.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value = (0,0,1,1)
    obj.data.materials.append(mat)
    
    obj = data.objects['stamen5']
    obj.color = (0.814,0.396,0.536,1)
    mat = data.materials.new("pink-white")
    mat.use_nodes = True
    mat.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value = (0,0,1,1)
    obj.data.materials.append(mat)
    
    obj = data.objects['stamen6']
    obj.color = (0.814,0.396,0.536,1)
    mat = data.materials.new("pink-white")
    mat.use_nodes = True
    mat.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value = (0,0,1,1)
    obj.data.materials.append(mat)
    
    obj = data.objects['stamen7']
    obj.color = (0.814,0.396,0.536,1)
    mat = data.materials.new("pink-white")
    mat.use_nodes = True
    mat.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value = (0,0,1,1)
    obj.data.materials.append(mat)
    
    obj = data.objects['stamen8']
    obj.color = (0.814,0.396,0.536,1)
    mat = data.materials.new("pink-white")
    mat.use_nodes = True
    mat.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value = (0,0,1,1)
    obj.data.materials.append(mat)
    
    obj = data.objects['stamen9']
    obj.color = (0.814,0.396,0.536,1)
    mat = data.materials.new("pink-white")
    mat.use_nodes = True
    mat.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value = (0,0,1,1)
    obj.data.materials.append(mat)
    
    obj = data.objects['stamen10']
    obj.color = (0.814,0.396,0.536,1)
    mat = data.materials.new("pink-white")
    mat.use_nodes = True
    mat.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value = (0,0,1,1)
    obj.data.materials.append(mat)

def generate_petals():
    '''Generate five cherry blossom petals.'''
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

    # Rotations and translations for other four petals
    trans_p2 = (2.55, 1.8, 0.0)
    trans_p3 = (-0.83, 3.18, -0.04) # 0.007, 0.025, -0.03
    trans_p4 = (-3.25, -0.17, 0.0)
    trans_p5 = (-0.95, -2.95, 0.0) 
    trans_petal = [trans_p2, trans_p3, trans_p4, trans_p5]

    rot_petal = 70    
    for i in range(1,5):
        # duplicate first petal four times and apply rot and trans
        ops.object.duplicate_move()
        ops.transform.rotate(value = -math.radians(rot_petal), orient_axis = 'Z')
        ops.transform.translate(value = trans_petal[i-1]) 

    # move petals into 'petal' collection and call next part generation
    ops.object.select_all(action = 'SELECT')
    ops.object.move_to_collection(collection_index = 1)
    generate_stamen_base()

if __name__ == '__main__':
    generate_petals()
