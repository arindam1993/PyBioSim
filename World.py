'''
Created on Jan 16, 2015

@author: Arindam
'''
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
import os

class World(object):
    
    def __init__(self, width, height):
        self.agents=[]
        self.obstacles=[]
        self.balls=[]
        self.width = width
        self.height = height
        
    def draw(self, loopIndex, imageDirName):
        
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d') 
        ax.set_xlim3d(-self.width,self.width)
        ax.set_ylim3d(-self.width,self.width)
        ax.set_zlim3d(-self.height,self.height)
        for agent in self.agents:
            agent.draw(ax)
        for obstacle in self.obstacles:
            obstacle.draw(ax)
        for ball in self.balls:
            ball.draw(ax)
        fname = imageDirName + '/' + str(int(100000000+loopIndex)) + '.png' # name the file 
        savefig(fname, format='png')
        print 'Written'+ fname
        plt.close()
        
        


        