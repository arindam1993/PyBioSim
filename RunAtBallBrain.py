'''
Created on Feb 6, 2015

@author: Arindam
'''
from Agent import Agent
from Ball import Ball
from Obstacle import Obstacle
from LinearAlegebraUtils import getYPRFromVector
class RunAtBallBrain(object):
    '''
    classdocs
    '''


    def __init__(self, agent, world):
        '''
        Constructor
        '''
        self.agent = agent
        self.world = world        
        

    def takeStep(self, myTeam=[], enemyTeam=[], balls=[], obstacles=[]):
        return balls[0].position, getYPRFromVector(balls[0].position)
        

        