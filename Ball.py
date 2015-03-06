'''
(c) 2015 Georgia Tech Research Corporation
This source code is released under the New BSD license.  Please see the LICENSE.txt file included with this software for more information

authors: Arindam Bose (arindam.1993@gmail.com), Tucker Balch (trbalch@gmail.com)
'''


import numpy as np
from numpy.linalg.linalg import norm
from LinearAlegebraUtils import normalize, reflectVector
from numpy import array
from SimTime import SimTime
from numpy import *

class Ball(object):
    '''
    classdocs
    '''


    def __init__(self, position):
        '''
        Constructor
        '''
        self.position = position.astype(double)
        self.radius = 5
        self.uid = id(self)
        self.isKinematic = True
        self.velocity = array([0, 0, 0])
        
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
        if self.isKinematic:
            moveVector = position - self.position
            moveVector = normalize(moveVector)
            self.position += moveVector * float(speed)
            
    def updatePhysics(self):
        if not self.isKinematic:
            self.position += self.velocity * SimTime.fixedDeltaTime
#             print "Ballin to"+str(self.velocity * SimTime.fixedDeltaTime)
            self.velocity *= 0.99  

            #Handle floor collisions
            if self.position[2] < -100:
                self.position[2] = -100 + 0.1
                self.velocity = reflectVector(self.velocity, array([0, 0, 1]))
            if self.position[2] > 100:
                self.position[2] = 100 - 0.1
                self.velocity = reflectVector(self.velocity, array([0, 0, -1]))
            if self.position[1] < -100:
                self.position[1] = -100 + 0.1
                self.velocity = reflectVector(self.velocity, array([0, 1, 0]))
            if self.position[1] > 100:
                self.position[1] = 100 - 0.1
                self.velocity = reflectVector(self.velocity, array([0, -1, 0]))
            if self.position[0] < -100:
                self.position[0] = -100 + 0.1
                self.velocity = reflectVector(self.velocity, array([1, 0, 0]))
            if self.position[0] > 100:
                self.position[0] = 100 - 0.1
                self.velocity = reflectVector(self.velocity, array([-1, 0, 0]))
            #clamp ball speed
            mag = np.linalg.norm(self.velocity)
            if mag > 200:
                self.velocity = normalize(self.velocity) * 200
            
            
    def kick(self, direction, intensity):
        directionNorm = normalize(direction)
        if not self.isKinematic:
            self.velocity = directionNorm * intensity
        
    def getUID(self):
        return self.uid
    
    def setUID(self, uid):
        self.uid = uid
        
    def makePhysics(self):
        self.isKinematic = False
    
    