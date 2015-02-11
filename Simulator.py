'''
Created on Jan 16, 2015

@author: Arindam
'''

import numpy as np
import matplotlib.pyplot as plt
from numpy import *
from World import *
from Agent import Agent
from Obstacle import *
from pylab import *
import os
from Ball import Ball
from matplotlib import animation
from LinearAlegebraUtils import distBetween
from RunAtBallBrain import RunAtBallBrain
from Team import Team


#Called once for initialization
'''
Usage guidelines:
1. Define globals required for the simulation in the __init__ constructor, here we define a bunch of waypoints for the ball
2. Initialize the globals in the setup() method. 
'''

class Simulator(object):
    def __init__(self, world, simTime, fps, imageDirName):
        self.world = world
        self.simTime = simTime
        self.fps = fps
        self.imageDirName = imageDirName
        self.currWP = 0
        self.ballWPs = [array([50, -100, 0]), array([0, 100, -70]), array([50, 20, 100]),array([-30, 50, -100]), array([100, -100, 100])]

    def setup(self):    
        #setup directory to save the images
        self.imageDirName = 'images'
        try:
            os.mkdir(self.imageDirName)
        except:
            print self.imageDirName + " subdirectory already exists. OK."

        #defining the brain for the agent
        brain = RunAtBallBrain()
        #define teams which the agents can be a part of
        teamA = Team("A", '#ff99ff')
        teamB = Team("B", '#ffcc99')
        #Defining a couple of agents 
        ag1Pos = array([80, 50, -20])
        ag1Rot = array([30, 0, 0])
        agent1 = Agent(teamA, ag1Pos, ag1Rot, brain, 5, 5)
        
        
        ag2Pos = array([-80, 0, 0])
        ag2Rot = array([0, 0, 0])
        agent2 = Agent(teamA, ag2Pos, ag2Rot, brain, 5, 5)
        
        ag3Pos = array([70, 30, 50])
        ag3Rot = array([0, 0, 0])
        agent3 = Agent(teamB, ag3Pos, ag3Rot, brain, 5, 5)
        
        ag4Pos = array([-80, 20, 60])
        ag4Rot = array([0, 0, 0])
        agent4 = Agent(teamB, ag4Pos, ag4Rot, brain, 5, 5)
        
        #Add the agent to the world
        self.world.agents.append(agent1)
        self.world.agents.append(agent2)
        self.world.agents.append(agent3)
        self.world.agents.append(agent4)
        
        #define a bunch of obstacles
        ob1Pos = array([-50,-50,-50])
        ob1 = Obstacle(ob1Pos, 30)
        
        ob2Pos = array([80,-50,-50])
        ob2 = Obstacle(ob2Pos, 20)
        
        #add obstacles to the world
        self.world.obstacles.append(ob1);
        self.world.obstacles.append(ob2)
        
        #define a ball
        ball = Ball(array([0, 0, 0]))
        
        
        #add the ball to the world
        self.world.balls.append(ball)
        


    
#Called repeatedly to create the movie
    def loop(self,loopIndex, ax):
        
        self.world.draw(ax)
        for agent in self.world.agents:
            agent.moveAgent(self.world)
        
        for ball in self.world.balls:  
            if len(self.ballWPs) > 0:  
                ball.moveBall(self.ballWPs[0], 6)
                if distBetween(ball.position, self.ballWPs[0]) < 5:
                    if len(self.ballWPs) > 0:
                        self.ballWPs.remove(self.ballWPs[0])
                
    def run(self):
        #Run setup once
        self.setup()
        
        #Setup loop
        timeStep = 1/double(self.fps)
        currTime = double(0)
        loopIndex = 0
        while(currTime < self.simTime):
            fig = plt.figure(figsize=(16,12))
            ax = fig.add_subplot(111, projection='3d') 
            ax.view_init(elev = 30)
            self.loop(loopIndex, ax)
            fname = self.imageDirName + '/' + str(int(100000000+loopIndex)) + '.jpg' # name the file 
            savefig(fname, format='jpg', bbox_inches='tight')
            print 'Written Frame No.'+ str(loopIndex)+' to '+ fname
            plt.close()
            loopIndex+=1
            currTime+=double(timeStep)
            
    
        


#Simulation runs here
#set the size of the world
world = World(100, 100)
#specify which world to simulate, total simulation time, and frammerate for video
sim = Simulator(world, 30, 30, "images")
#run the simulation
sim.run()
# os.system("ffmpeg -f image2 -i "1%08d.jpg" -r 30 outPut.mp4")
    