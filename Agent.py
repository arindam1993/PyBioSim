'''
Created on Jan 16, 2015

@author: Arindam
'''
import numpy as np
from numpy import *
from LinearAlegebraUtils import rotMatrixFromYPR
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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
        self.up = cross(self.forward, self.right)       #unit vector pointing upwards
 
    '''
    Plots a sphere of radius 10 with a left hand co-ordinate frame on the provided subplot.
    '''       
    def draw(self, subplot): 
        
        ##plots the sphere           
        u = np.linspace(0, 2 * np.pi, 30)
        v = np.linspace(0, np.pi, 30)

        x = self.drawRadius * np.outer(np.cos(u), np.sin(v)) + self.position[0]
        y = self.drawRadius * np.outer(np.sin(u), np.sin(v)) + self.position[1]
        z = self.drawRadius * np.outer(np.ones(np.size(u)), np.cos(v)) + self.position[2]
        if self.team == "A":
            sphereColor = '#ff99ff'
        if self.team == "B":
            sphereColor = '#ffcc99'
        subplot.plot_surface(x, y, z,  rstride=4, cstride=4, color=sphereColor)
        
        #plots the left handed co-ordinate Frame
        
        #plots the forward a red line
        fw = self.position + self.forward * (self.drawRadius + 10)
        x_fw = array([self.position[0], fw[0]])
        y_fw = array([self.position[1], fw[1]])
        z_fw = array([self.position[2], fw[2]])
        subplot.plot(x_fw, y_fw, z_fw, color='r')
        
        #plots the right as a blue line
        ri = self.position + self.right * (self.drawRadius + 10)
        x_ri = array([self.position[0], ri[0]])
        y_ri = array([self.position[1], ri[1]])
        z_ri = array([self.position[2], ri[2]])
        subplot.plot(x_ri, y_ri, z_ri, color='b')
        
        #plots up as a green Line
        up = self.position + self.up * (self.drawRadius + 10)
        x_up = array([self.position[0], up[0]])
        y_up = array([self.position[1], up[1]])
        z_up = array([self.position[2], up[2]])
        subplot.plot(x_up, y_up, z_up, color='g')