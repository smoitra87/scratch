"""
This program uses the scickit-learn library to learn a lasso 
regression model

"""

import numpy as np
import pylab as pl
from sklearn import linear_model 

print __doc__


n_samples, n_features = 50,200
X = np.random.randn(n_samples,n_features)
w = 3*np.random.randn(n_features) # Just to increase coeff range
w[10:] = 0 # Introduce some sparsity
y = np.dot(X,w)

#######################################################################
# Create the Training and Testing Set
#######################################################################

X_train, y_train = X[:n_samples/2], y[:n_samples/2]
X_test, y_test = X[n_samples/2:], y[n_samples/2:]

#######################################################################
# Train the Lasso model
#######################################################################

alpha = 0.1
clf = linear_model.Lasso(alpha=alpha)
clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)

# Calculate the prediction accuracies
print 'The prediction accuracy is %f' % (1-
np.linalg.norm(y_pred-y_test)**2/ (np.linalg.norm(y_test))**2 )

# Plot the y_test and the y_pred values
pl.scatter(y_test,y_pred,color='black')
pl.xlabel('y_test')
pl.ylabel('y pred')
pl.title('Scatter plot between test and predicted values')
pl.show()
