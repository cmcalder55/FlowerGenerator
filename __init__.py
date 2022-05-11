
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
from os import system, path
from bpy import data, types, ops
from bpy.utils import register_class, unregister_class
import make_flower

# current filepath and callable directories
filepath = data.filepath
dir = path.dirname(filepath)

# Ensure current directory is callable by the base path
if not dir in sys.path:
   sys.path.append(dir)

# clear interpreter console
clear = lambda: system('cls')
clear() 

class GenerateFlower(types.Operator):

    # class properties
    bl_idname = 'object.generate_petals'
    bl_label = 'flower'
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(self, context):
        return context.mode == 'OBJECT'
    
    def execute(self, context):
        return self.invoke(context, None)
        
    def invoke(self, context, event):
        make_flower.generate_petals()
        
        return {'FINISHED'}
	
# class registration/unregistration
def register():
	register_class(GenerateFlower)

def unregister():
	unregister_class(GenerateFlower)

# register class and call with default settings from Blender
register()
ops.object.generate_petals('INVOKE_DEFAULT')

# for testing only
# if __name__ == "__main__":
#     register()