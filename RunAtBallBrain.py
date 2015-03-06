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
class RunAtBallBrain(object):
    '''
    classdocs
    '''


    def __init__(self):      
        pass
    
    def takeStep(self, myTeam=[], enemyTeam=[], balls=[], obstacles=[]):
        actions = []
        deltaPos = np.array([1, 0, 0])
        deltaRot = getYPRFromVector(balls[0].position)
        myTeamName = myTeam[0].team.name
        for agent in enemyTeam:
            if myTeamName == 'A':
                actions.append(Stun(agent, 10))
        for ball in balls:
            actions.append(Kick(ball, np.array([1, 0, 0]), 100))
        return deltaPos, deltaRot, actions
        

        