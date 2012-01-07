#! /usr/bin/env python 
"""
Solves the diabetes problem by doing LARS
"""

print __doc__

import numpy as np
import pylab as pl
from sklearn.linear_model import lars_path
from sklearn.datasets import load_diabetes

diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target

#######################################################################
# train the lars model

alphas, active, coefs = lars_path(X,y,method='lasso',verbose=True)
xx = np.sum(np.abs(coefs.T),axis=1)
xx /= xx[-1]
pl.plot(xx,coefs.T)
ymin,ymax = pl.ylim()
pl.vlines(xx,ymin,ymax,linestyle='--')

pl.xlabel('|coef/max(coef)|')
pl.ylabel('Coefficients')
pl.title('Plot of coefficients in LARS Lasso')
pl.axis('tight')
pl.show()
