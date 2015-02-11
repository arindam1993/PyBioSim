'''
Created on Feb 6, 2015

@author: Arindam
'''
from Agent import Agent
from Ball import Ball
from Obstacle import Obstacle
from LinearAlegebraUtils import getYPRFromVector
import numpy as np
class RunAtBallBrain(object):
    '''
    classdocs
    '''


    def __init__(self):      
        pass
    
    def takeStep(self, myTeam=[], enemyTeam=[], balls=[], obstacles=[]):
        deltaPos = np.array([1, 0, 0])
        deltaRot = getYPRFromVector(balls[0].position)
        return deltaPos, deltaRot
        

        