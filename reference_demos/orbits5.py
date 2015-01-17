#
# Simulate planets with gravity. Requires numpy and matplotlib. 
# The program places a series of images in the subdirectory "orbits."
# You will have to assemble them into a movie.
#
# by Tucker Balch (tucker@cc.gatech.edu)
# October 2011
#

# imports
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pylab import *
import os

# start here
imagedir = "orbits5"
try:
	os.mkdir(imagedir)
except:
	print imagedir + " subdirectory already exists. OK."

seconds = 600000.0 # how long to run in seconds
fps = 0.1 # frames per second
frames = seconds * fps # how many frames for whole movie
firstframe = 100000 # this is used to create the filename

numobjs = 5 # number of planets
poshistpoints = fps * 1000  # how long to make the trails

np.random.seed(seed=6)
mfactor = 100000 # a mass factor to scale things
pos = np.random.uniform(low=-2, high=2, size=(numobjs,3)) # positions
poshist = np.zeros((numobjs,poshistpoints,3)) # position history for tails
mass = np.random.normal(loc=.05, scale=0.1, size=numobjs) # masses
mass = mass*mass/mfactor # square in case negative
vel = np.random.uniform(low=-.01, high=.01, size=(numobjs,3)) # initial vels
vel[:,2]=0 # make sure no up/down velocity
acc = np.zeros([numobjs,3]) # acceleration
colors = []
for i in range(0,numobjs):
	colors.append([0,1,0])
dead = np.zeros([numobjs,1])

# set special conditions for "sun"
pos[0,:] = [0,0,0]
vel[0,:] = [0,0,0]
mass[0] = 100.0 / mfactor
colors[0]=[1,0,0]

# set special conditions for "planet"
#pos[1,:] = [3,0,0]
#vel[1,:] = [0,0.005,0]
#mass[1] = 0.1 / mfactor
#colors[1]=[0,0,1]

# set special conditions for "moon"
#pos[2,:] = [3.2,0,0]
#vel[2,:] = [0,0000.005,0.001]
#mass[2] = 0.0005 / mfactor
#colors[2]=[1,1,0]

# set special conditions for "planet"
#pos[3,:] = [4,0,0]
#vel[3,:] = [0,0.005,0.0]
#mass[3] = 0.1 / mfactor
#colors[3]=[0,0,1]

vel = vel/fps
for i in range(0,numobjs):
	for j in range(0,int(poshistpoints)):
		poshist[i,j,:] = pos[i,:]

for i in np.arange(firstframe,firstframe+frames+1): #for all the frames
	t = i / fps # where we are (in seconds)
	fig = plt.figure()
	ax = fig.add_subplot(111,projection='3d')
	ax.scatter(pos[:,0],pos[:,1],pos[:,2], # show our planets \
		s = np.sqrt(mass)*mfactor, # Size is related to mass \
		alpha = 0.5, edgecolors='none', c = colors)
	for j in range(0,numobjs): # plot the trails
		ax.plot(poshist[j,:,0],\
		poshist[j,:,1],\
		poshist[j,:,2],\
		linewidth=2,\
		alpha = 0.3)
	fname = imagedir + '/' + str(int(i)) + '.png' # name the file 
	print fname
	ax.set_xlim3d(-4,4)
	ax.set_ylim3d(-4,4)
	ax.set_zlim3d(-4,4)
	#savefig(fname, format='png') # save it
	plt.show()
	plt.close() # close or we get a massive memory leak

	# update acceleration, vel, pos
	for i in range(0,numobjs): # gravitation is N^2
		affect = np.zeros(numobjs)
		dist = np.zeros(numobjs)
		acc[i,:] = [0,0,0]
		for j in range(0,numobjs):
			diff = pos[i]-pos[j]
			diff = sum(diff * diff)
			if (diff==0):
				diff = 0.00000001
			dist = sqrt(diff)
			affect = mass[j]/(dist*dist)
			vec = affect*(pos[j]-pos[i])/dist/fps
			acc[i,:] = acc[i,:] + vec
			# check if dead
			if i != 1 and j==0 and diff > 1.1:
				 colors[i] = [0,1,0]
			if i != 0 and j==0 and diff <= 1.1:
				colors[i] = [0,0,1]
			if (i != 0 and j==0 and diff <= 1.0) or dead[i]==1:
				vel[i] = [0,0,0]
				acc[i] = [0,0,0]
				colors[i] = [0,0,0]
				dead[i]=1
				mass[i] = mass[i] * 0.989
	vel = vel + acc
	pos = pos + vel
	#pos[-1,:] = [0,0,0]
	# shift the location history
	for j in range(0,int(poshistpoints-1)):
		poshist[:,j,:] = poshist[:,j+1,:]
	for j in range(0,numobjs):
		poshist[j,-1,:] = pos[j]
