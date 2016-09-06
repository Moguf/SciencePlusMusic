import bpy

class SimpleOperator(bpy.types.Operator):
    """ example """

def register():
    bpy.utils.register_class(SimpleOperator)

def unregister():
    bpy.utils.unregister_class(SimpleOperator)


if __name__ == "__main__":
    register()
