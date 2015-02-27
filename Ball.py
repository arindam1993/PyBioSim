'''
Created on Jan 16, 2015
Ball or attractor

@author: Arindam
'''

import numpy as np
from numpy.linalg.linalg import norm
from LinearAlegebraUtils import normalize

class Ball(object):
    '''
    classdocs
    '''


    def __init__(self, position):
        '''
        Constructor
        '''
        self.position = position.astype(float)
        self.radius = 5
        
    def draw(self,subplot):
        #draw a sphere of specified size at specified position
        u = np.linspace(0, 2 * np.pi, 25)
        v = np.linspace(0, np.pi, 25)

        x = self.radius * np.outer(np.cos(u), np.sin(v)) + self.position[0]
        y = self.radius * np.outer(np.sin(u), np.sin(v)) + self.position[1]
        z = self.radius * np.outer(np.ones(np.size(u)), np.cos(v)) + self.position[2]
        subplot.plot_surface(x, y, z,  rstride=4, cstride=4, linewidth = 0, color='w')
        
    def moveBall(self, position, speed):
        #move the ball to specified position at the specified speed, speed is distance per frame  
        moveVector = position - self.position
        moveVector = normalize(moveVector)
        self.position += moveVector * float(speed)
    
    