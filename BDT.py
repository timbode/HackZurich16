 # -*- coding: utf-8 -*-
import os, sys
import itertools
import random
import numpy as np

from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier

class BoostedDecisionTree():
        def __init__(self, n_estimators, max_depth, min_samples_leaf, trainingSet, labels):
                self.n_estimators=n_estimators
                self.max_depth=max_depth
                self.min_samples_leaf=min_samples_leaf
                self.BDT=AdaBoostClassifier(DecisionTreeClassifier(max_depth=self.max_depth, min_samples_leaf=self.min_samples_leaf), algorithm="SAMME", n_estimators=self.n_estimators)
                self.BDT.fit(trainingSet, labels)
                self.predictedLabels=[]
                
        def predict(self, toBePredicted):
                self.predictedLabels=self.BDT.predict(toBePredicted)
