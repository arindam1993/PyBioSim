'''
Created on Jan 16, 2015
Representation of an obstacle in the world
@author: Arindam
'''
import numpy as np

class Obstacle(object):
    '''
    classdocs
    '''


    def __init__(self, position, radius):
        '''
        Constructor
        '''
        self.position = position
        self.radius = radius
        
    def draw(self, subplot):
        #draw a sphere of specified size at specified position
        u = np.linspace(0, 2 * np.pi, 50)
        v = np.linspace(0, np.pi, 50)

        x = self.radius * np.outer(np.cos(u), np.sin(v)) + self.position[0]
        y = self.radius * np.outer(np.sin(u), np.sin(v)) + self.position[1]
        z = self.radius * np.outer(np.ones(np.size(u)), np.cos(v)) + self.position[2]
        subplot.plot_surface(x, y, z,  rstride=4, cstride=4, linewidth = 0, shade = True, color='#ffff00')