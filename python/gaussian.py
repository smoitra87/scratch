"""
   Some experiments with Normal distribution

	1. Print and view standard normal gaussian distribution in 1D
       2. Print a view a Standard normal gaussian in 2D
       3. Print a view the effects of skewing a gaussian distribution
       4. Transform the axes of the gaussian according to eigen decomposition
      
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlb
import os,sys

#import scipy.stats.distribution.norm as normal


""" Print and view standard normal gaussian distribution in 1D """
  
x  = np.linspace(-5,5,100)

def norm_pdf(x,mu,sigma) :
    return 1. / (np.sqrt(2*np.pi)*sigma)*np.exp(-0.5*(x-mu)**2)

y = map(lambda(x) : norm_pdf(x,0,1),x)

fig = plt.figure() ;
ax = fig.gca()
plt.plot(x,y,label="Univariate Std normal")
plt.show()
#plt.close()

""" Print a std normal gaussian in 2D """
X = x;
Y = X;
X,Y = np.meshgrid(X,Y)

def norm_bivariate_pdf(x,mu,cov) :
    prec = np.linalg.inv(cov)
    return None
    









