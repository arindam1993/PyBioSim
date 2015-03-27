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
from NavUtils import getObstacleAvoidance, getTeamNearestAvoidance, getRestrictionField
class PreyBrain(object):
    '''
    classdocs
    '''


    def __init__(self):      
        pass
    
    def takeStep(self, myTeam=[], enemyTeam=[], balls=[], obstacles=[]):
        actions = []
        deltaPos = np.array([1, 0, 0])
        avoidMovement = getObstacleAvoidance(obstacles)
        avoidEnemyMovement = getTeamNearestAvoidance(enemyTeam)
        fenceAvoidMovement = getRestrictionField(obstacles[1], 200)
        movement = 1.5*avoidMovement + 2.0 * avoidEnemyMovement + 1.5*fenceAvoidMovement
        deltaRot = getYPRFromVector(movement)
        
        return deltaPos, deltaRot, actions
        

        