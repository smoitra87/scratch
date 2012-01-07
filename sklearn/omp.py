#! /usr/bin/env python

"""
Orthogonal pursuit matching and subplots
"""

print __doc__

import numpy as np
import pylab as pl

from  sklearn.linear_model import orthogonal_mp
from sklearn.datasets import make_sparse_coded_signal

n_components, n_features = 512,100
n_atoms = 17
# generate the data
###################

# y = Dx
# |x|_0 = n_atoms

y, D, x = make_sparse_coded_signal(n_samples=1,
                                   n_components=n_components,
                                   n_features=n_features,
                                   n_nonzero_coefs=n_atoms,
                                   random_state=0)

idx, = x.nonzero()

# distort the clean signal 
y_noisy = y + 0.05*np.random.randn(len(y))

# plot the sparse signal
pl.subplot(3,1,1)
pl.xlim(0,512)
pl.stem(idx,x[idx])
pl.title('Sparse signal')

# Plot the noise-free reconstruction
x_r = orthogonal_mp(D,y,n_atoms)
idx_r, = x_r.nonzero()
pl.subplot(3,1,2)
pl.xlim(0,512)
pl.stem(idx_r,x_r[idx_r])
pl.title('Recovered signal from noise-free measurements')

# plot the noisy reconstruction
x_r = orthogonal_mp(D,y_noisy,n_atoms)
idx_r, = x_r.nonzero()
pl.subplot(3,1,3)
pl.xlim(0,512)
pl.title('Recovered signal from noisy measurements')
pl.stem(idx_r,x_r[idx_r])

pl.suptitle('Sparse signal recovery with orthogonal matching pursuit',
fontsize=16)
pl.subplots_adjust(wspace=0.3,hspace=0.4)

pl.show()






