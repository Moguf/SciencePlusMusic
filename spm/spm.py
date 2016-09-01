#!/usr/bin/env python3
# fileencoding:utf-8

import subprocess

import scipy as sc
import matplotlib.pyplot as plt
from scipy.io.wavfile import read

from easyutil import MemUtil
mem = MemUtil()
mem.set(3)

class SPM(object):
    def __init__(self, wavfile):
        self.wavfile = wavfile
        self.late = 0
        self.data = []
        
    def main(self):
        self.loadWAV()
        self.testPlot()
        
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
        pass

    
if __name__ == '__main__':
    tmp = SPM('../datas/sounds/4943.wav')
    tmp.main()
