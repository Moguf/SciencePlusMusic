#!/usr/bin/env python3
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import numpy as np

fig = plt.figure()
ax = p3.Axes3D(fig)
Writer = animation.writers['ffmpeg']
writer = Writer(fps=150, bitrate=7200)

dt = 0.02
p = 10
r = 28
b = 8/3
xdata = [1.0]
ydata = [1.0]
zdata = [1.0]

def Lorenz(xdata,ydata,zdata):
    for num in range(20000):
        x = xdata[num-1]
        y = ydata[num-1]
        z = zdata[num-1]
        dx = dt*(-p*x + p*y)
        dy = dt*(-x*z + r*x - y)
        dz = dt*(x*y - b*z)
        xdata.append(x + dx) 
        ydata.append(y + dy)
        zdata.append(z + dz)

def show(num, xdata,ydata,zdata,line):
    line.set_data([xdata[:num:2], ydata[:num:2]])
    line.set_3d_properties(zdata[:num:2])
    #ax.plot(xdata,ydata,zdata)
    return line


ax.set_xlim3d([-50.0, 50.0])
ax.set_xlabel('X')

ax.set_ylim3d([-50.0, 50.0])
ax.set_ylabel('Y')

ax.set_zlim3d([-50.0, 50.0])
ax.set_zlabel('Z')

ax.set_title('3D Test')

Lorenz(xdata,ydata,zdata)

line = ax.plot(xdata,ydata,zdata,'-')[0]
line_ani = animation.FuncAnimation(fig, show, 9999, fargs=(xdata, ydata, zdata, line), interval=10, blit=False)

line_ani.save('rolenz.mp4',writer=writer)

