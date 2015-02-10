'''
Created on Feb 5, 2015

@author: Arindam
'''
from Agent import Agent
from abc import ABCMeta, abstractmethod
from Simulator import world

class Brain(object):
    __metaclass__ = ABCMeta
    '''
    Represents the brain of a particular agent
    '''


    def __init__(self, agent):
        pass
    def getMovementDecision(self, world):
        pass
    def buildEgoCentricRepresentationOfWorld(self, world):
        pass
    def takeStep(self, myTeam = [], enemyTeam = [], balls = [], obstacles = []):
        pass
        
    