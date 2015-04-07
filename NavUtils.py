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
    distToSurface = np.linalg.norm(currObstacle.position) - currObstacle.radius;
    if(distToSurface < 0.1):
        distToSurface = 0.1
    mag = 20/distToSurface;
    direction = currObstacle.position * -1
    if mag < 0:
        mag = 0
    return mag * direction;



def findNearestUnstunned(agents):
    unstunned = []
    for agent in agents:
        if not agent.isStunned:
            unstunned.append(agent)
    #using a lambda function to get the agent closest
    minAgent = min(unstunned, key = lambda a: np.linalg.norm(a.position))
    return minAgent;


def getTeamAvoidance(team):
    checkRange = 50
    vecSum = np.array([0, 0, 0])
    for agent in team:
        dist = np.linalg.norm(agent.position)
        if dist < checkRange:
            vecSum += (agent.position * -1)
    return vecSum ;

def getTeamNearestAvoidance(team):
    currAgent = team[0]
    for agent in team:
        if np.linalg.norm(agent.position) < np.linalg.norm(currAgent.position):
             currAgent = agent;
    #distance to surface
    distToSurface = np.linalg.norm(currAgent.position) - currAgent.colRadius;
    if(distToSurface < 0.1):
        distToSurface = 0.1
    mag = 20/distToSurface;
    direction = currAgent.position * -1
    if mag < 0:
        mag = 0
    return mag * direction;


def getRestrictionField(originObject, restrictionRange):
    pos = originObject.position
    dist = np.linalg.norm(pos)
    direction = normalize(pos)
    mag = 0
    if dist > (0.8)*restrictionRange:
        mag = dist
    else:
        mag = 0
    return mag*direction
