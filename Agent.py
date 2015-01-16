'''
Created on Jan 16, 2015

@author: Arindam
'''
from numpy import *
from LinearAlegebraUtils import rotMatrixFromYPR

class Agent(object):
    '''
    An Agent class which encapsulates the begaviour of the agent.
    classdocs
    '''


    def __init__(self, team, position, rotation, colRadius, drawRadius):
        self.position = position        #numpy array [x, y ,z]
        self.rotation = rotation        #numpy array [yaw, pitch, roll] (in degrees)
        self.colRadius = colRadius      #float size of collision sphere
        self.drawRadius = drawRadius    #float size of sphere to be drawn
        self.team = team                #provide team 'A' or team 'B'
        self.forward = dot(array([1, 0, 0]), rotMatrixFromYPR(rotation))    #unit vector in forward direction of agent
        self.right = dot(array([0, 1, 0]), rotMatrixFromYPR(rotation))      #unit vector in right direction of agent
        self.up = cross(self.forward, self.right)