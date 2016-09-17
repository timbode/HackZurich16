import BDT
import random
from math import *
import numpy as np

import matplotlib
import matplotlib.pyplot as plt


N=40000
M=10000
randomVectors=[]
randomLabel=[]
for i in xrange(N):
        v=[random.uniform(-1,1), random.uniform(-1,1), random.uniform(-1,1), random.uniform(-1,1), 0, 0]
        absV1=np.sqrt(v[0]*v[0]+v[1]*v[1])
        absV2=np.sqrt(v[2]*v[2]+v[3]*v[3])
        v=[v[0]/absV1, v[1]/absV1, v[2]/absV2, v[3]/absV2, absV1, absV2]
        randomVectors.append(v)
        randomLabel.append(0)
        
vectors=[]
label=[]
for i in xrange(M):
        rand=random.uniform(-1,1)
        v=[rand, random.uniform(-1,1), -rand, random.uniform(-1,1), 0, 0]
        absV1=np.sqrt(v[0]*v[0]+v[1]*v[1])
        absV2=np.sqrt(v[2]*v[2]+v[3]*v[3])
        v=[v[0]/absV1, v[1]/absV1, v[2]/absV2, v[3]/absV2, absV1, absV2]
        vectors.append(v)
        label.append(1)

n_estimators=500
max_depth=3
min_samples_leaf=10
trainingSet=randomVectors+vectors
labels=randomLabel+label

randomVectors=[]
for i in xrange(N):
        v=[random.uniform(-1,1), random.uniform(-1,1), random.uniform(-1,1), random.uniform(-1,1), 0, 0]
        absV1=np.sqrt(v[0]*v[0]+v[1]*v[1])
        absV2=np.sqrt(v[2]*v[2]+v[3]*v[3])
        v=[v[0]/absV1, v[1]/absV1, v[2]/absV2, v[3]/absV2, absV1, absV2]
        randomVectors.append(v)
        
vectors=[]
for i in xrange(M):
        rand=random.uniform(-1,1)
        v=[rand, random.uniform(-1,1), -rand, random.uniform(-1,1), 0, 0]
        absV1=np.sqrt(v[0]*v[0]+v[1]*v[1])
        absV2=np.sqrt(v[2]*v[2]+v[3]*v[3])
        v=[v[0]/absV1, v[1]/absV1, v[2]/absV2, v[3]/absV2, absV1, absV2]
        vectors.append(v)

tree=BDT.BoostedDecisionTree(n_estimators, max_depth, min_samples_leaf, trainingSet, labels)
toBePredicted=randomVectors+vectors
tree.predict(toBePredicted)


plt.figure(figsize=(10, 10))
twoclass_output = tree.BDT.decision_function(toBePredicted)
classified=[]
notClassified=[]
plot_range = (twoclass_output.min(), twoclass_output.max())
plt.subplot(111)
for k, x in enumerate(labels):
        if x==1:
                classified.append(twoclass_output[k])
        else: 
                notClassified.append(twoclass_output[k])
plt.hist(classified, bins=50, range=plot_range, alpha=.3, color='green')
plt.hist(notClassified, bins=50, range=plot_range, alpha=.3, color='red')

plt.savefig('plot.png')
