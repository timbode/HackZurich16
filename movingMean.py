# -*- coding: utf-8 -*-
import os, sys
from numpy import *

class MovingMean():
        def __init__(self, N, values):
                self.N=N 
                self.values=values
                self.movingMeans=[]
        
        def getMean(self):
                for i, value in enumerate(self.values):
                        if i>=self.N-1:
                                mM=0
                                for k in xrange(self.N):
                                        mM+=self.values[i-k]
                                mM=mM/self.N
                                self.movingMeans.append(mM)
