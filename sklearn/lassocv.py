"""
Performs  CV for Lasso 
"""

print __doc__

import numpy as np
import pylab as pl
from sklearn.linear_model import LassoCV, LassoLarsCV, LassoLarsIC
from sklearn import datasets
import time

diabetes = datasets.load_diabetes()
X = diabetes.data
y = diabetes.target

rng = np.random.RandomState(42)
X = np.c_[X,rng.randn(X.shape[0],14)]

# normalize the data so that it is compatible with LARS
X /= np.sqrt(np.sum(X**2,axis=0))

#######################################################################
# Perform LassoCV
#######################################################################

print "computing regularization path using LARS CV"
t1 = time.time()
model = LassoCV(cv=20).fit(X,y)
t_lasso_cv = time.time() - t1
print "Time taken to compute Lasso CV %s secs" % t_lasso_cv

# Display the results
m_log_alphas =  -np.log10(model.alphas)
m_mse = model.mse_path_

pl.figure()
ymin,ymax=  2300,3800
pl.plot(m_log_alphas,m_mse,':')
pl.plot(m_log_alphas,m_mse.mean(axis=1),linewidth=3,color='black',
label="average across the folds")
pl.ylim(ymin,ymax)
pl.axvline(-np.log10(model.alpha),linestyle='--',color='k',label=
'CV alpha')

pl.legend()
pl.xlabel('-log(alpha)')
pl.ylabel('fold error')
pl.title('Plot of fold error vs alpha')
pl.axis('tight')



#######################################################################
# Perform LassoLarsIC with AIC and BIC
#######################################################################

model_aic = LassoLarsIC(criterion='aic');
t1 = time.time()
model_aic.fit(X,y)
print "Time taken to calculate AIC is %f" % (time.time()-t1)

model_bic = LassoLarsIC(criterion="bic")
model_bic.fit(X,y)



# plot the results
def plot_IC_plots(model,col) : 
	criterion = model.criterion
	pl.axvline(-np.log10(model.alpha_),color=col,label=criterion+
	' alpha',linewidth=3)
	pl.plot(-np.log10(model.alphas_),model.criterion_,linestyle="--",
	linewidth=2,label=criterion+' criteria',color=col)

pl.figure()
plot_IC_plots(model_aic,'red');
plot_IC_plots(model_bic,'blue')

pl.legend()
pl.xlabel('-log(alphas)')
pl.ylabel('IC criteria')
pl.title('Plot of various information criteria')
ymin,ymax = 3500,4000
pl.ylim(ymin,ymax)


pl.show()


