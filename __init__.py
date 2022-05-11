'''
Install Blender as a Python module: https://wiki.blender.org/wiki/Building_Blender/Other/BlenderAsPyModule
Install blenderpy module: https://github.com/TylerGubala/blenderpy  
Python API documentation: https://docs.blender.org/api/current/index.html   
'''
bl_info = {
    'name': 'Flower Generator',
    'description': 'Generate cherry blossoms.',
    'author': 'Cameron Calder, Paul Tziranis',
    'version': (1, 0),
    'blender': (3, 0, 1),
    'location': 'View3D > Add > Mesh',
    'warning': '',
    'doc_url':'https://github.com/cmcalder55/FlowerGenerator',
    'category': 'Add Mesh',
}

import sys 
from os import system

sys.path.append("C:\\Users\\camer\\blender_ws\\FlowerGenerator")

from bpy import data, types, ops
from bpy.utils import register_class, unregister_class
from cherryblossom import make_flower


# clear interpreter console
clear = lambda: system('cls')
clear() 

class GenerateFlower(types.Operator):

    # class properties
    bl_idname = 'mesh.generate_petal'
    bl_label = 'flower'
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):

        make_flower()
        
        return {'FINISHED'}
	
# module registration
def register():
	register_class(GenerateFlower)

def unregister():
	unregister_class(GenerateFlower)

if __name__ == "__main__":
    
    register()
    # ops.mesh.generate_petal()
