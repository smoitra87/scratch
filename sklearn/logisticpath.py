#! /usr/bin/env python
"""
This computes the logistic regression path using L1 reg
"""

print __doc__

import numpy as np
import pylab as pl
from datetime import datetime

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.svm import l1_min_c


iris = load_iris()
X = iris.data
y = iris.target

# make the classification problem into a binary classification problem
X = X[y!=2]
y = y[y!=2]

X -= X.mean(0) # normalize the data

#######################################################################
# Perform the logistic regression
cs = l1_min_c(X,y,loss='log') * np.logspace(0,3)

print 'Computing regularization path now'
start = datetime.now()
clf = LogisticRegression(C=1., penalty='l1',tol=1e-6)
coefs = []

for c in cs :
	clf.set_params(C=c)
	clf.fit(X,y)
	coefs.append(clf.coef_.ravel())

print 'Logistic Regression path took',(datetime.now()-start)
coefs = np.array(coefs)
pl.plot(np.log10(cs),coefs)
pl.xlabel('Log10(cs)')
pl.ylabel('Coefficients')
pl.title('Plot of Logistic Regression path')
pl.axis('tight')

pl.show()


