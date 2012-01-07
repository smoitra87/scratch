#! /usr/bin/env python

"""
Performs Bayesian Ridge Regression
"""

print __doc__

import numpy as np
import pylab as pl
from sklearn.linear_model import BayesianRidge, LinearRegression
from scipy import stats
import time

#######################################################################
# Generating simulated data
np.random.seed(0)
n_samples, n_features = 100,100
X = np.random.randn(n_samples,n_features)
lambda_ = 4 # This is the precision for w
w = np.zeros(n_features)

# Select the number of relevant features
relevant = np.random.randint(0,n_features,10)
for i in relevant : 
	w[i] = stats.norm.rvs(loc=0,scale = 1./np.sqrt(lambda_))
# create noise with precision = 50
alpha_ = 50
noise = stats.norm.rvs(loc=0,scale=1./np.sqrt(alpha_),size=n_samples)
y = np.dot(X,w) + noise;
	
#######################################################################
# Fit the Bayesian Ridge Regression and OLS for comparison
t1 = time.time()
clf = BayesianRidge(compute_score=True)
clf.fit(X,y)
print 'time elapsed Bayesian %f' % (time.time()-t1)

t1 = time.time()
ols = LinearRegression()
ols.fit(X,y)
print 'time elapsed OLS %f' % (time.time() - t1)

#######################################################################
# Plot true weights, estimated weights and histogram of weights
pl.figure(figsize=(6,5))
pl.title('Weights of the model')
pl.plot(clf.coef_,'b-',label='Bayesian coefs')
pl.plot(ols.coef_, 'r--',label='OLS coefs')
pl.plot(w,'g-',label='ground truth')
pl.xlabel('param ids')
pl.ylabel('param values')
pl.legend(loc="best",prop=dict(size=12))

pl.figure(figsize=(6,5))
pl.hist(clf.coef_,bins=n_features,log=True)
pl.plot(clf.coef_[relevant],5*np.ones(len(relevant)),'ro',
label='relevant coefs')
pl.title('Histogram of the coefficient values')
pl.xlabel('Values of parameters')
pl.ylabel('Counts of params')
pl.legend(loc="upper left")

pl.figure(figsize=(6,5))
pl.title('Marginal Log likelihood')
pl.plot(clf.scores_)
pl.ylabel('marginal log likelihood')
pl.xlabel('Iterations')

pl.show()




