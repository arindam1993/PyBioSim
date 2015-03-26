'''
(c) 2015 Georgia Tech Research Corporation
This source code is released under the New BSD license.  Please see the LICENSE.txt file included with this software for more information

authors: Arindam Bose (arindam.1993@gmail.com), Tucker Balch (trbalch@gmail.com)
'''

from Agent import Agent
from Ball import Ball
from Obstacle import Obstacle
from LinearAlegebraUtils import *
import numpy as np
from Action import Stun, Kick
import random
from NavUtils import getObstacleAvoidance
class PredatorBrain(object):
    '''
    classdocs
    '''


    def __init__(self):      
        pass
    
    def takeStep(self, myTeam=[], enemyTeam=[], balls=[], obstacles=[]):
        actions = []
        deltaPos = np.array([1, 0, 0])
        nearestUnstunnedAgent = self.findNearestUnstunned(enemyTeam)
        stunMovement = array([0, 0, 0])
        if nearestUnstunnedAgent.isStunned:
            stunMovement  = array([0, 0, 0])
        else:
            stunMovement = nearestUnstunnedAgent.position

        avoidMovement = getObstacleAvoidance(obstacles)

        movement = normalize(1.5*stunMovement + 0.5*avoidMovement)
        deltaRot = getYPRFromVector(movement)
        actions.append(Stun(nearestUnstunnedAgent, 5))

        return deltaPos, deltaRot, actions




    def findNearestUnstunned(self, agents):
        currAgent = agents[0]
        for agent in agents:
            if not agent.isStunned:
                if np.linalg.norm(agent.position) < np.linalg.norm(currAgent.position):
                    currAgent = agent
        return currAgent;

        