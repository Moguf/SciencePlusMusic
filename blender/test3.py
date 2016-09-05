import os
import bpy
import numpy as np

bpy.ops.mesh.primitive_cube_add(location=(1,1,1))

bpy.data.objects['Camera'].location = (10,10,10)
bpy.data.objects['Camera'].rotation_euler = (0,0,0)
bpy.data.cameras['Camera'].lens = 10

bpy.data.objects['Lamp'].location = (0,0,30)
bpy.data.lamps['Lamp'].type = 'SUN'



bpy.context.scene.render.resolution_x = 1920
bpy.context.scene.render.resolution_y = 1080
bpy.context.scene.render.resolution_percentage = 100
bpy.context.scene.render.image_settings.file_format = 'FFMPEG'

bpy.data.scenes['Scene'].render.filepath = 'test3.mp4'
bpy.context.scene.frame_start = 0
bpy.context.scene.frame_end = 20
bpy.ops.render.render(animation=True)
savePath=os.path.abspath(os.path.dirname(__file__))
bpy.path.relpath(savePath)
