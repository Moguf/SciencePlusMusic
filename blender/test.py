import bpy
import numpy

for item in bpy.context.scene.objects:
    if item.type == 'MESH':
        bpy.context.scene.objects.unlink(item)
for item in bpy.data.objects:
    if item.type == 'MESH':
        bpy.data.objects.remove(item)
for item in bpy.data.meshes:
    bpy.data.meshes.remove(item)
for item in bpy.data.materials:
    bpy.data.materials.remove(item)
    
dt = 0.02
p = 10
r = 28
b = 8/3
xdata = [1.0]
ydata = [1.0]
zdata = [1.0]
bpy.context.scene.frame_end   = 2000

def Lorenz(xdata,ydata,zdata):
    for num in range(4000):
        x = xdata[num-1]
        y = ydata[num-1]
        z = zdata[num-1]
        dx = dt*(-p*x + p*y)
        dy = dt*(-x*z + r*x - y)
        dz = dt*(x*y - b*z)
        xdata.append(x + dx) 
        ydata.append(y + dy)
        zdata.append(z + dz)
        

bpy.ops.object.camera_add(
    location=(70, -40, 50),
    rotation=(1.1, 0, 0.8)
)

Lorenz(xdata,ydata,zdata)

number_of_frame = 0
bpy.ops.mesh.primitive_ico_sphere_add(subdivisions = 3, size = 3, location = (1, 1, 1))

for i,j,k in zip(xdata[::2], ydata[::2], zdata[::2]):
    bpy.context.scene.frame_set(number_of_frame)
    obj = bpy.context.scene.objects.active
    obj.location = (i, j, k)
    obj.keyframe_insert( data_path='location' )
    number_of_frame += 1
