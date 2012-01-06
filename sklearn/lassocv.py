"""
Performs  CV for Lasso 
"""

import numpy as np
import pylab as pl
from sklearn.linear_model import LassoCV, LassoLarsCV, LassoLarsIC
from sklearn import datasets

diabetes = datasets.load_diabetes()
X = diabetes.data


