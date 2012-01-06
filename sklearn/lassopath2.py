"""
  Plot the Lasso and Elastic Net paths
"""

print __doc__

import numpy as np
import pylab as pl
from sklearn.linear_model import lasso_path, enet_path
from sklearn.datasets import load_diabetes

diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target

X /= X.std(0)


#######################################################################
# Calculate the Lasso and the enet paths
#######################################################################
eps = 5e-3;

models = lasso_path(X,y,eps=eps)
alphas_lasso = np.array([model.alpha for model in models])
coefs_lasso = np.array([model.coef_ for model in models])

models = enet_path(X,y,eps=eps,rho=0.7)
alphas_enet = np.array([model.alpha for model in models])
coefs_enet = np.array([model.coef_ for model in models])

#######################################################################
# Plot the paths
#######################################################################

ax = pl.gca()
ax.set_color_cycle(2*['b','g','r','c','k'])
l1 = pl.plot(coefs_lasso)
l2 = pl.plot(coefs_enet,linestyle='--')

pl.xlabel('-Log(Lambda)')
pl.ylabel('Coefficients')
pl.title('Path taken by lasso coefficients')
pl.legend((l1[-1],l2[-1]),('lasso','enet'),loc='lower left')
pl.axis('tight')
pl.show()
