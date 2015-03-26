'''
(c) 2015 Georgia Tech Research Corporation
This source code is released under the New BSD license.  Please see the LICENSE.txt file included with this software for more information

authors: Arindam Bose (arindam.1993@gmail.com), Tucker Balch (trbalch@gmail.com)
'''
from LinearAlegebraUtils import *
import numpy as np


    

def getObstacleAvoidance(obstacles):
    currObstacle = obstacles[0]
    for obstacle in obstacles:
        if np.linalg.norm(obstacle.position) < np.linalg.norm(currObstacle.position):
             currObstacle = obstacle;
    #distance to surface
    distToSurface = np.linalg.norm(currObstacle.position) - obstacle.radius;
    if(distToSurface < 0.1):
        distToSurface = 0.1
    mag = 20/distToSurface;
    direction = obstacle.position * -1
    if mag < 0:
        mag = 0
    return mag * direction;



def findNearestUnstunned(agents):
    currAgent = agents[0]
    for agent in agents:
        if not agent.isStunned:
            if np.linalg.norm(agent.position) < np.linalg.norm(currAgent.position):
                    currAgent = agent
    return currAgent;


def getTeamAvoidance(team):
    checkRange = 50
    vecSum = np.array([0, 0, 0])
    for agent in team:
        dist = np.linalg.norm(agent.position)
        if dist < checkRange:
            if(dist < 0.1):
                dist=0.1
            vecSum+=normalize(agent.position)*20/dist
    return vecSum * -1;
