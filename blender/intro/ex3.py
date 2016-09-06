import bpy
class BaseOperator:
    def execute(self, context):
        print('Hello World BaseClass')
        return {'FINISHED'}


class SimpleOperator(bpy.types.Operator, BaseOperator):
    bl_idname = 'object.simple_operator'
    bl_label = 'Tool Name'

bpy.utils.register_class(SimpleOperator)
