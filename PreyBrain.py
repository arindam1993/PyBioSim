'''
(c) 2015 Georgia Tech Research Corporation
This source code is released under the New BSD license.  Please see the LICENSE.txt file included with this software for more information

authors: Arindam Bose (arindam.1993@gmail.com), Tucker Balch (trbalch@gmail.com)
'''

from Agent import Agent
from Ball import Ball
from Obstacle import Obstacle
from LinearAlegebraUtils import getYPRFromVector
import numpy as np
from Action import Stun, Kick
from NavUtils import getObstacleAvoidance, getTeamNearestAvoidance
class PreyBrain(object):
    '''
    classdocs
    '''


    def __init__(self):      
        pass
    
    def takeStep(self, myTeam=[], enemyTeam=[], balls=[], obstacles=[]):
        actions = []
        deltaPos = np.array([1, 0, 0])
        ballMovement = balls[0].position
        avoidMovement = getObstacleAvoidance(obstacles)
        avoidEnemyMovement = getTeamNearestAvoidance(enemyTeam)
        movement = ballMovement  + 1.5*avoidMovement + 3.0 * avoidEnemyMovement
        deltaRot = getYPRFromVector(movement)
        
        return deltaPos, deltaRot, actions
        

        