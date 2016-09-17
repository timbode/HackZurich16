# -*- coding: utf-8 -*-
import os, sys
from numpy import *

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

params={
'font.size': 14,
'mathtext.default' : 'rm' # see http://matplotlib.org/users/customizing.html
}
matplotlib.rcParams['agg.path.chunksize']=20000
matplotlib.rcParams.update(params)

import getTrajectories as gT

getTrajec=gT.GetTrajectories()
getTrajec.getFiles()
getTrajec.getDataAndCuts()
getTrajec.cutData()
getTrajec.formTrajectories()

cleanData=getTrajec.cleanData()
for fileName in cleanData:
        print len(cleanData[fileName]), len(getTrajec.data[fileName])


cuts=getTrajec.cuts
allTrajectories=getTrajec.allTrajectories

getTrajec.normalizeTrajectories()
        
getTrajec.formVelocities()
allVelocities=getTrajec.allVelocities

getTrajec.formVelocityAngles()
allDifferences=getTrajec.allVelocityAngles

getTrajec.formMovingMeans()
allMovingMeans=getTrajec.allMovingMeans
        
for fileName in allDifferences:
        for index in allDifferences[fileName]:
                plots={}
                #print allDifferences[fileName][index]
                #print allTrajectories[fileName][index]
                y0=[d for d in allDifferences[fileName][index]]
                x1=[d[0][0] for d in allTrajectories[fileName][index]]
                y1=[d[0][1] for d in allTrajectories[fileName][index]]
                y2=allVelocities[fileName][index]
                x3=allMovingMeans[fileName][index][0][0]
                y3=allMovingMeans[fileName][index][0][1]
                fig=plt.figure(figsize=(20,10))
                plots[0]=plt.subplot(1,3,1)
                plots[1]=plt.subplot(1,3,2)
                plots[2]=plt.subplot(1,3,3)
                plots[0].set_title('$Angle\ between\ velocity\ vectors\ against\ time$')
                plots[1].set_title('$Trajectory$')
                plots[2].set_title('$Velocity$')
                plots[0].plot([t for t in xrange(len(y0))],y0)
                plots[0].set_ylim(-1.0, 1.0)
                plots[0].axhline(0, color='grey')
                plots[1].plot(x1,y1)
                plots[0].set_xlabel('$t$')
                plots[1].set_xlabel('$x$')
                plots[2].set_xlabel('$t$')
                plots[0].set_ylabel('$cos(\phi)$')
                plots[1].set_ylabel('$y$')
                plots[2].set_ylabel('$\sqrt{||v||^{2}}$')
                plots[1].set_xlim(min(x1), max(x1))
                plots[1].set_ylim(min(y1), max(y1))
                plots[1].axvline(0, color='grey')
                plots[1].axhline(0, color='grey')
                plots[2].plot([t+1 for t in xrange(len(y2))],y2)
                fig.tight_layout()
                fig.savefig(fileName+'_'+index+'.png')
                plt.close()
                
