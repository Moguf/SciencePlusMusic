#!/usr/bin/env python3
# fileencoding:utf-8

import subprocess
import numpy as np
import scipy as sc
import matplotlib
import  matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import matplotlib.animation as animation
from scipy.io.wavfile import read

#from easyutil import MemUtil
#mem = MemUtil()
#mem.set(3)

class SPM(object):
    def __init__(self, wavfile):
        self.wavfile = wavfile
        self.late = 0
        self.data = []
        self.nframe = 100
        
    def main(self):
        self.loadWAV()
        self.animation()
        
    def loadWAV(self):
        self.rate, self.data = read(self.wavfile)
        self.left = self.data[:, 0]
        self.right = self.data[:, 1]

    def testPlot(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(self.left[::100])
        ax.plot(self.right[::100])
        plt.show()

    def animation(self):
        fig = plt.figure()
        x = np.arange(-3, 3, 0.25)
        y = np.arange(-3, 3, 0.25)
        X, Y = np.meshgrid(x, y)
        Z = np.sin(X) + np.cos(X)

        ims = []
        xdata = []
        ydata = []
        zdata = []

        for t in range(4):
            ax = Axes3D(fig)
            Z = np.sin(X + t) + np.cos(Y + t)
            img = ax.plot_wireframe(X, Y, Z)
            ims.append(img)
        ani = animation.ArtistAnimation(fig, ims, interval=1)
        plt.show()
        

if __name__ == '__main__':
    tmp = SPM('../datas/sounds/4943.wav')
    tmp.main()
