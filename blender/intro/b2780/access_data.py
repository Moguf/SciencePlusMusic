import bpy

## Accessing DataBlocks
print(bpy.data.objects)
print(bpy.data.scenes)
print(bpy.data.materials)
## About Collections
print(list(bpy.data.objects))
print(bpy.data.objects['Cube'])
print(bpy.data.objects[0])
## Accessing Attributes
print(bpy.data.objects[0].name)
print(bpy.data.scenes['Scene'])
print(bpy.data.materials.new('MyMaterial'))
print(bpy.data.scenes[0].render.resolution_percentage)
#print(bpy.data.scenes[0].objects['Torus'].data.vertices[0].co.x)
## Data Creation/Removal
#print(bpy.types.Mesh())
mesh = bpy.data.meshes.new(name='MyMesh')
print(mesh)
bpy.data.meshes.remove(mesh)
print(mesh)

## Context( read-only)
print(bpy.context.object)
print(bpy.context.selected_objects)
print(bpy.context.visible_bones)
# (NG) bpy.context.object = obj
# (OK) bpy.context.scene.objects.active = obj

## Operators (Tools)
#print(bpy.ops.mesh.flip_normals())
#print(bpy.ops.mesh.hide(unselected=False))
#print(bpy.ops.object.scale_apply())

## Operator Poll() # check the cursor in valid area.
#print(bpy.ops.view3d.render_border())
if bpy.ops.view3d.render_border.poll():
    bpy.ops.view3d.render_border()


## integration
# defining a rendering engine
# defining operators
# defining menus, headers and panels
# inserting new buttos int existing menus, headers and panels

