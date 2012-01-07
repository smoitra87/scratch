#! /usr/bin/env python

"""
Perform logistic regression with L1 L2 regularization
"""
print __doc__

import numpy as np
import pylab as pl

from sklearn.linear_model import LogisticRegression
from sklearn import datasets

iris = datasets.load_iris()

X = iris.data
y = iris.target

# Loop over the regularization parameter

for c in [0.1,1,10] :
	clf_l1_LR = LogisticRegression(C=c,penalty='l1')
	clf_l2_LR = LogisticRegression(C=c,penalty='l2')
	clf_l1_LR.fit(X,y)
	clf_l2_LR.fit(X,y)
	
	coef_l1_LR = clf_l1_LR.coef_
	coef_l2_LR = clf_l2_LR.coef_
	
	sparsity_l1_LR = np.mean(coef_l1_LR==0) * 100
	sparsity_l2_LR = np.mean(coef_l2_LR==0) * 100
	
	print "C=%f" % (c)
	print "L1 sparsity percentage - %f" % (sparsity_l1_LR)
	print "L2 sparsity percentage - %f" % (sparsity_l2_LR)
