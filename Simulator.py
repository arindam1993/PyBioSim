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


#Called once for initialization

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

        
        #Defining a couple of agents 
        ag1Pos = array([80, 50, -20])
        ag1Rot = array([30, 0, 0])
        agent1 = Agent("A", ag1Pos, ag1Rot, 5, 5)
        
        
        ag2Pos = array([-80, 0, 0])
        ag2Rot = array([0, 0, 0])
        agent2 = Agent("A", ag2Pos, ag2Rot, 5, 5)
        
        ag3Pos = array([70, 30, 50])
        ag3Rot = array([0, 0, 0])
        agent3 = Agent("B", ag3Pos, ag3Rot, 5, 5)
        
        ag4Pos = array([-80, 20, 60])
        ag4Rot = array([0, 0, 0])
        agent4 = Agent("B", ag4Pos, ag4Rot, 5, 5)
        
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
        
        #Wire up the agent with brains
        ag1Brain = RunAtBallBrain(agent1, self.world)
        ag2Brain = RunAtBallBrain(agent2, self.world)
        ag3Brain = RunAtBallBrain(agent3, self.world)
        ag4Brain = RunAtBallBrain(agent4, self.world)
        agent1.addBrain(ag1Brain)
        agent2.addBrain(ag2Brain)
        agent3.addBrain(ag3Brain)
        agent4.addBrain(ag4Brain)
    
#Called repeatedly to create the movie
    def loop(self,loopIndex, ax):
        
        
        self.world.draw(ax)
        for agent in self.world.agents:
#             print "Position"+str(agent.position)+"Forward"+str(agent.forward)
            agent.moveAgent(self.world)
        
        for ball in self.world.balls:  
            if len(self.ballWPs) > 0:  
                ball.moveBall(self.ballWPs[0], 6)
                if distBetween(ball.position, self.ballWPs[0]) < 5:
    #                 self.currWP += 1
                    if len(self.ballWPs) > 0:
                        self.ballWPs.remove(self.ballWPs[0])
    #                 if(self.currWP > len(ballWPs) - 1 ):
    #                     self.currWP = len(ballWPs) - 1
                
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
            print 'Written Frame No.'+loopIndex+' to '+ fname
            #plt.show()
            plt.close()
            loopIndex+=1
#             print currTime
            currTime+=double(timeStep)
            
    
        


#Simulation runs here
world = World(100, 100)
sim = Simulator(world, 120, 30, "images")
sim.run()
# os.system("ffmpeg -f image2 -i "1%08d.jpg" -r 30 outPut.mp4")
    