# -*- coding: utf-8 -*-
import os, sys
from numpy import *

import movingMean

class GetTrajectories():
        def __init__(self):
                self.files=[]
                self.data={}
                self.cuts={}
                self.allTrajectories={}
                self.allVelocities={}
                self.allVelocityAngles={}
                self.allMovingMeans={}
                
        def getFiles(self):
                for fileName in os.listdir(os.getcwd()):
                        if '.dat' in fileName:
                                print fileName
                                self.files.append(fileName)
                                
        def getDataAndCuts(self):
                for fileName in self.files:
                        d=[]
                        with open(fileName) as f:
                                for i, line in enumerate(f):
                                        if line.startswith('='): self.cuts[fileName]=i
                                        d.append(line.strip().split())
                        self.data[fileName]=d
                        
        def cutData(self):
                for fileName in self.cuts: 
                        self.data[fileName]=self.data[fileName][self.cuts[fileName]+2:-1]
                        
        def formTrajectories(self):
                for fileName in self.data:
                        trajectories={}
                        for d in self.data[fileName]:
                                trajectories[d[3]]=[]
                        for d in self.data[fileName]:
                                trajectories[d[3]].append([[float(d[0]),float(d[1])],int(d[2]),int(d[4])])
                        self.allTrajectories[fileName]=trajectories
                        
        def normalizeTrajectories(self):
                for fileName in self.allTrajectories:
                        for index in self.allTrajectories[fileName]:
                                trajectory=self.allTrajectories[fileName][index]
                                t0=trajectory[0][1]
                                x0=trajectory[0][0][0]
                                y0=trajectory[0][0][1]
                                self.allTrajectories[fileName][index]=[[[d[0][0]-x0,d[0][1]-y0],d[1]-t0,d[2]] for d in trajectory]
        
        def getDifferences(self, ofThis, target, lam):
                for i in xrange(len(ofThis)):
                        if i==0: continue
                        x=lam(ofThis[i][0], ofThis[i-1][0])
                        y=lam(ofThis[i][1], ofThis[i-1][1])
                        target.append([x, y])
        
        def getAbsValue(self, OfThis):
                return sqrt(OfThis[0]*OfThis[0]+OfThis[1]*OfThis[1])
        
        def formVelocities(self):
                for fileName in self.allTrajectories:
                        velocities={}
                        for index in self.allTrajectories[fileName]:
                                velocities[index]=[]
                                
                                difference=[]
                                self.getDifferences([[d[0][0],d[0][1]] for d in self.allTrajectories[fileName][index]], difference, lambda x, y: x-y)
                                
                                for i in xrange(len(difference)):
                                        if i==0: continue
                                        abs1=self.getAbsValue(difference[i])
                                        velocities[index].append(abs1)
                        self.allVelocities[fileName]=velocities
                        
        def formVelocityAngles(self):
                for fileName in self.allTrajectories:
                        differencesOfDifferences={}
                        trajectories=self.allTrajectories[fileName]
                        for index in trajectories:
                                trajectory=trajectories[index]
                                
                                difference=[]
                                self.getDifferences([[d[0][0],d[0][1]] for d in trajectory], difference, lambda x, y: x-y)
                                
                                differenceOfDifferences=[]
                                
                                vDiff=[]
                                self.getDifferences(difference, vDiff, lambda x, y: x*y)
                                
                                for i in xrange(len(difference)):
                                        if i==0: continue
                                        x=vDiff[i-1][0]
                                        y=vDiff[i-1][1]
                                        abs1=self.getAbsValue(difference[i])
                                        abs2=self.getAbsValue(difference[i-1])
                                        denom=abs1*abs2+1e-6
                                        differenceOfDifferences.append((x+y)/denom)
                                differencesOfDifferences[index]=differenceOfDifferences
                        self.allVelocityAngles[fileName]=differencesOfDifferences
                        
        def formMovingMeans(self):
                for fileName in self.allTrajectories:
                        trajectories=self.allTrajectories[fileName]
                        self.allMovingMeans[fileName]={}
                        for index in trajectories:
                                self.allMovingMeans[fileName][index]=[]
                                trajectory=trajectories[index]
                                difference=[]
                                self.getDifferences([[d[0][0],d[0][1]] for d in trajectory], difference, lambda x, y: x-y)
                                N=10
                                mMX=movingMean.MovingMean(N, [d[0] for d in difference])
                                mMX.getMean()
                                mMY=movingMean.MovingMean(N, [d[1] for d in difference])
                                mMY.getMean()
                                self.allMovingMeans[fileName][index].append([mMX.movingMeans, mMY.movingMeans])
                
        def cleanData(self):
                newData={}
                for fileName in self.data:
                        newData[fileName]=[]
                        dat=self.data[fileName]
                        i=0
                        while i<len(dat):
                                dat[i]=[float(x) for x in dat[i]]
                                if dat[i][4]==0:
                                        newData[fileName].append(dat[i])
                                counter1=1
                                if dat[i][4]==1:
                                        tmp=dat[i]
                                        #print 'here', dat[i]
                                        while dat[i+counter1][4]=='1':
                                                dat[i+counter1]=[float(x) for x in dat[i+counter1]]
                                                #print 'here too',counter1, dat[i+counter1], '\t'
                                                tmp=[(tmp[k]+dat[i+counter1][k]) for k in xrange(len(tmp))]
                                                counter1+=1
                                        newData[fileName].append([tmp[k]/counter1 for k in xrange(len(tmp))])
                                i+=counter1
                return newData
                                
                                
