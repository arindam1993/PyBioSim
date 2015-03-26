
from Agent import Agent
from Ball import Ball
from Obstacle import Obstacle
from LinearAlegebraUtils import *
import numpy as np
from Action import Stun, Kick
import random
    

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