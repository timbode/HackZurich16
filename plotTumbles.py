# -*- coding: utf-8 -*-
import os, sys
import numpy as np
from math import *
import json

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

params={
'font.size': 14,
'mathtext.default' : 'rm' # see http://matplotlib.org/users/customizing.html
}
matplotlib.rcParams['agg.path.chunksize']=20000
matplotlib.rcParams.update(params)

def getAbs(values):
        return sqrt(values[0]*values[0]+values[1]*values[1])+1e-6, sqrt(values[2]*values[2]+values[3]*values[3])+1e-6

def scalarProduct(values):
        return values[0]*values[2]+values[1]*values[3]

allTumbles=[]
with open('allTumbles.json', 'r') as infile:
        allTumbles=json.load(infile)
        
allOther=[]
with open('allOther.json', 'r') as infile:
        allOther=json.load(infile)

angleThreshold=0.5

allTumbleAngles=[]
allTumbleVelocities1=[]
allTumbleVelocities2=[]
for event in allTumbles:
        values=event['v']
        abs1, abs2=getAbs(values)
        x=scalarProduct(values)/(abs1*abs2)
        #if x > angleThreshold: continue
        allTumbleAngles.append(x)
        allTumbleVelocities1.append(abs1)
        allTumbleVelocities2.append(abs2)

allOtherAngles=[]
allOtherVelocities1=[]
allOtherVelocities2=[]
for event in allOther:
        values=event['v']
        abs1, abs2=getAbs(values)
        x=scalarProduct(values)/(abs1*abs2)
        #if x > angleThreshold: continue
        allOtherAngles.append(x)
        allOtherVelocities1.append(abs1)
        allOtherVelocities2.append(abs2)
        
        
plots={}
fig=plt.figure(figsize=(15,5))
bins=50
plots[0]=plt.subplot(1,2,1)
plots[0].hist(allTumbleAngles, bins=bins, color='green', alpha=.3)
plots[0].set_title('$Histogram\ of\ angles\ between\ velocities\ for\ tumbles$')
plots[0].set_xlabel('$cos(\phi)$')
plots[1]=plt.subplot(1,2,2)
plots[1].hist(allOtherAngles, bins=bins, color='red', alpha=.3)
plots[1].set_title('$Histogram\ of\ angles\ between\ velocities\ for\ no\ tumbles$')
plots[1].set_xlabel('$cos(\phi)$')
#plots[1].set_ylim(0,1000)
fig.tight_layout()
fig.savefig('allAngles.png')
plt.close()
fig=plt.figure(figsize=(15,5))
plots[2]=plt.subplot(1,2,1)
plots[2].hist(allTumbleVelocities1, bins=bins, color='lightgreen', alpha=.2)
plots[2].hist(allTumbleVelocities2, bins=bins, color='darkgreen', alpha=.2)
plots[2].set_title('$Histogram\ of\ velocities\ before\ and\ after\ tumbles$')
plots[2].set_xlabel('$\sqrt{||v||^{2}}$')
plots[3]=plt.subplot(1,2,2)
plots[3].hist(allOtherVelocities1, bins=bins, color='red', alpha=.2)
plots[3].hist(allOtherVelocities2, bins=bins, color='darkred', alpha=.2)
plots[3].set_title('$Histogram\ of\ velocities\ before\ and\ after\ no\ tumbles$')
plots[3].set_xlabel('$\sqrt{||v||^{2}}$')
fig.tight_layout()
fig.savefig('allVelocities.png')
plt.close()

plots={}
fig=plt.figure(figsize=(20,10))
bins=50
plots[0]=plt.subplot(1,2,1)
plots[0].scatter(allTumbleAngles, allTumbleVelocities2, color='green', s=.1)
plots[0].set_title('$Angles\ vs.\ velocities\ for\ tumbles$')
plots[0].set_xlim(-1,1)
plots[0].set_ylim(0)
plots[0].set_xlabel('$cos(\phi)$')
plots[0].set_ylabel('$\sqrt{||v||^{2}}$')
plots[1]=plt.subplot(1,2,2)
#plots[1].scatter(allTumbleAngles, allTumbleVelocities1, s=.3)
plots[1].scatter(allOtherAngles, allOtherVelocities1, color='red', s=.1)
plots[1].set_title('$Angles\ vs.\ velocities\ for\ no\ tumbles$')
plots[1].set_xlim(-1,1)
plots[1].set_ylim(0)
plots[1].set_xlabel('$cos(\phi)$')
plots[1].set_ylabel('$\sqrt{||v||^{2}}$')
fig.tight_layout()
fig.savefig('correlations.png')
plt.close()
