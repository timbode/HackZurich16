# -*- coding: utf-8 -*-
import os, sys
from numpy import *
import json

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

params={
'font.size': 12,
'mathtext.default' : 'rm' # see http://matplotlib.org/users/customizing.html
}
matplotlib.rcParams['agg.path.chunksize']=20000
matplotlib.rcParams.update(params)

import getTrajectories as gT

def makeDict(trajectory, fileName, index):
        pt=[trajectory[i-1][0], trajectory[i][0], trajectory[i+1][0]]
        lam=lambda x, y: x-y
        xi=lam(pt[1][0], pt[0][0])
        yi=lam(pt[1][1], pt[0][1])
        xf=lam(pt[2][0], pt[1][0])
        yf=lam(pt[2][1], pt[1][1])
        event={}
        event["fileName"]=fileName
        event["index"]=index
        event["t"]=trajectory[i][1]
        event["v"]=[xi,yi,xf,yf]
        return event

getTrajec=gT.GetTrajectories()
getTrajec.getFiles()
getTrajec.getDataAndCuts()
getTrajec.cutData()
cleanData=getTrajec.cleanData()
getTrajec.data=cleanData
getTrajec.formTrajectories()
getTrajec.normalizeTrajectories()

allTumbles=[]
allOther=[]
for fileName in getTrajec.allTrajectories:
        for index in getTrajec.allTrajectories[fileName]:
                trajectory=getTrajec.allTrajectories[fileName][index]
                for i in xrange(1, len(trajectory)-1):
                        if trajectory[i][2]==1:
                                allTumbles.append(makeDict(trajectory, fileName, index))
                        if trajectory[i][2]==0:
                                allOther.append(makeDict(trajectory, fileName, index))

with open('allTumbles.json', 'w') as outfile:
        json.dump(allTumbles, outfile)
        
with open('allOther.json', 'w') as outfile:
        json.dump(allOther, outfile)
