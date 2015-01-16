'''
Created on Jan 16, 2015
Some junk linear alegebra methods.
@author: Arindam
'''

from numpy import *

def rotMatrixFromYPR(rotation):
    a = math.radians(rotation[0])
    b = math.radians(rotation[1])
    c = math.radians(rotation[2])
    rotMat = array([
                    [math.cos(a)*math.cos(b), math.cos(a)*math.sin(b)*math.sin(c) - math.sin(a)*math.cos(c), math.cos(a)*math.sin(b)*math.cos(c) + math.sin(a)*math.sin(c)],
                    [math.sin(a)*math.cos(b), math.sin(a)*math.sin(b)*math.sin(c) + math.cos(a)*math.cos(c), math.sin(a)*math.sin(b)*math.cos(c) - math.cos(a)*math.sin(c)],
                    [-math.sin(b), math.cos(b)*math.sin(c), math.cos(b)*math.cos(c)]])
    return rotMat