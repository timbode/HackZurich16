import BDT
import random
from math import *
import numpy as np
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
trainingSet=[]
labels=[]
for event in allTumbles:
        values=event['v']
        abs1, abs2=getAbs(values)
        x=scalarProduct(values)/(abs1*abs2)
        #if x > angleThreshold: continue
        allTumbleAngles.append(x)
        allTumbleVelocities1.append(abs1)
        allTumbleVelocities2.append(abs2)
        trainingSet.append([x, abs1, abs2])
        labels.append(1)
        
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
        trainingSet.append([x, abs1, abs2])
        labels.append(0)

n_estimators=100
max_depth=3
min_samples_leaf=5
tree=BDT.BoostedDecisionTree(n_estimators, max_depth, min_samples_leaf, trainingSet, labels)
toBePredicted=trainingSet

tree.predict(toBePredicted)


plt.figure(figsize=(10, 10))
twoclass_output = tree.BDT.decision_function(toBePredicted)
classified=[]
notClassified=[]
plot_range = (twoclass_output.min(), twoclass_output.max())
plt.subplot(111)
plt.title('$Histogram\ of\ decision\ scores\ for\ BDT$')
plt.xlabel('$BDT\ score$')
plt.xlim(-1,1)
plt.ylim(0,1000)
for k, x in enumerate(labels):
        if x==1:
                classified.append(twoclass_output[k])
        else: 
                notClassified.append(twoclass_output[k])
plt.hist(classified, bins=50, range=plot_range, alpha=.3, color='green')
plt.hist(notClassified, bins=50, range=plot_range, alpha=.3, color='red')
plt.tight_layout()
plt.savefig('classified.png')

