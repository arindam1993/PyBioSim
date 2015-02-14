'''
Created on Jan 16, 2015
Some junk linear alegebra methods.
@author: Arindam
'''

from numpy import *
import numpy as np

def rotMatrixFromYPR(rotation):
    a = math.radians(rotation[0])
    b = -math.radians(rotation[1])
    c = math.radians(rotation[2])
    rotMat = array([
                    [math.cos(a)*math.cos(b), math.cos(a)*math.sin(b)*math.sin(c) - math.sin(a)*math.cos(c), math.cos(a)*math.sin(b)*math.cos(c) + math.sin(a)*math.sin(c)],
                    [math.sin(a)*math.cos(b), math.sin(a)*math.sin(b)*math.sin(c) + math.cos(a)*math.cos(c), math.sin(a)*math.sin(b)*math.cos(c) - math.cos(a)*math.sin(c)],
                    [-math.sin(b), math.cos(b)*math.sin(c), math.cos(b)*math.cos(c)]])
    rotMat = transpose(rotMat)
    return rotMat

def getYPRFromVector(vector):
    mag = math.sqrt(vector[0]*vector[0] + vector[1]*vector[1] )
    yaw = math.degrees(math.atan2(vector[1],vector[0]))
    pitch = math.degrees(math.atan2(vector[2], mag))
    roll = 0
    return array([yaw, pitch, roll])

def distBetween(p1, p2):
    distVec = p2 - p1
    return np.linalg.norm(distVec)

def normalize(vector):
    mag = np.linalg.norm(vector)
    return vector/mag

def clampRotation(rotation, maxRot):
    if rotation[0] > 0:
        if rotation[0] > maxRot[0]:
            rotation[0] = maxRot[0]
    elif rotation[0] < 0:
        if -1 * rotation[0] > maxRot[0]:
            rotation[0] = -1 * maxRot[0]
    if rotation[1] > 0:
        if rotation[1] > maxRot[1]:
            rotation[1] = maxRot[1]
    elif rotation[1] < 0:
        if -1 * rotation[1] > maxRot[1]:
            rotation[1] = -1 * maxRot[1]
    if rotation[2] > 0:
        if rotation[2] > maxRot[2]:
            rotation[2] = maxRot[2]
    elif rotation[2] < 0:
        if -1 * rotation[2] > maxRot[2]:
            rotation[2] = -1 * maxRot[2]
    return rotation
        
