import os
import bpy
import numpy as np


bpy.ops.mesh.primitive_circle_add(location=(4.0,4.0,4.0))
bpy.ops.mesh.primitive_cone_add(location=(4.0,0.0,0.0))
bpy.ops.mesh.primitive_cylinder_add(location=(10.0,0.0,0.0))
bpy.ops.mesh.primitive_cube_add(location=(0.0,4.0,0.0))
bpy.ops.mesh.primitive_grid_add(location=(10.0,10.0,10.0))
bpy.ops.mesh.primitive_monkey_add(location=(-10.0,0.0,0.0))
bpy.ops.mesh.primitive_monkey_add(location=(0.0,-10.0,0.0))
bpy.ops.mesh.primitive_plane_add(location=(0.0,-10.0,-10.0))
bpy.ops.mesh.primitive_torus_add(location=(0.0,-10.0,0.0))

bpy.data.objects['Camera'].location = (0,10,30)
bpy.data.objects['Camera'].rotation_euler = (0,-np.pi/6,0)
bpy.data.cameras['Camera'].lens = 10

bpy.data.objects['Lamp'].location = (0,0,30)
bpy.data.lamps['Lamp'].type = 'SUN'


bpy.context.scene.render.resolution_x = 1920
bpy.context.scene.render.resolution_y = 1080
bpy.context.scene.render.resolution_percentage = 100
bpy.context.scene.render.image_settings.file_format = 'AVI_JPEG'

bpy.data.scenes['Scene'].render.filepath = 'test3.avi'
bpy.context.scene.frame_start = 0
bpy.context.scene.frame_end = 1
bpy.ops.render.render(animation=True)
savePath=os.path.abspath(os.path.dirname(__file__))
bpy.path.relpath(savePath)
