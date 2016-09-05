import os
import bpy
import math

bpy.ops.object.delete()

N = 10
for x in range(0,N):
    for y in range(0,N):
        for z in range(0,N):
            bpy.ops.mesh.primitive_cube_add(location=(x*2,y*2,z*2))
            bpy.ops.rigidbody.object_add()

bpy.ops.mesh.primitive_plane_add(location=(N-1,N-1,-10))
bpy.ops.rigidbody.object_add(type='PASSIVE')
bpy.data.objects["Plane"].scale = (N+10,N+10,1)

bpy.data.objects['Camera'].location = (N+20,N+20,N+20)
bpy.data.objects['Camera'].rotation_euler = (math.pi/6,0,math.pi*3/4)
bpy.data.cameras['Camera'].lens = 10

bpy.data.objects['Lamp'].location = (0,0,N+10)
bpy.data.lamps['Lamp'].type = 'SUN'

bpy.ops.ptcache.bake_all()


bpy.context.scene.render.resolution_x = 400
bpy.context.scene.render.resolution_y = 400
bpy.context.scene.render.resolution_percentage = 100
bpy.context.scene.render.image_settings.file_format = 'AVI_JPEG'

bpy.data.scenes['Scene'].render.filepath = 'test.avi'
bpy.context.scene.frame_start = 0
bpy.context.scene.frame_start = 200
bpy.ops.render.render(animation=True)

savePath=os.path.abspath(os.path.dirname(__file__))
bpy.path.relpath(savePath)
bpy.ops.wm.save_as_mainfile(filepath='test.blend',relative_remap=True)

            
