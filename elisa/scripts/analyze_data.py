"""
Script for analyzing ELISA lysate data

Author:Subhodeep Moitra (smoitra@cs.cmu.edu)
"""

import numpy as np
import pylab as pl
import pdb

def run_pred_data() :
	# Load data from file 
	fname = "../data/rawdata.dat"
	with open(fname,"r") as fin :
		data = fin.readlines()
		data = np.array([float(val.strip()) for val in data ])
	data = data.reshape((7,9),order='F')
	input_prot = data[:,0]
	lysate = data[:,1:]
	nPoints,nSamples = lysate.shape
	
	# make a least squares fit
	mlist = [] # list of slopes
	rlist = [] # list of R2 coefficients
	clist = []
	pl.figure()
	ax = pl.gca()
	ax.set_color_cycle(['r','g','b','c','k','y','m','brown'])
	for i in range(nSamples) :
		A = np.vstack([input_prot, np.ones(nPoints)]).T
		y = lysate[:,i]
		coeffs,res = np.linalg.lstsq(A,y)[0:2]
		m,c = coeffs
		r2 = 1. - res/y.var() # calc r2 coeff
		rlist.append(r2)
		x = input_prot	
		pl.plot(x,m*x+c,'--',label='lysate'+str(i+1))
		mlist.append(m)
		clist.append(c)
	
		
	avg_m = np.array(mlist).mean()
	std_m = np.array(mlist).std()
	avg_r2 = np.array(rlist).mean()
	avg_c = np.array(clist).mean()
	
	print 'Average m', avg_m
	print 'Average c', avg_c
	
	pl.plot(input_prot,lysate,'o')
	pl.xlabel('conc')
	pl.ylabel('pred value')
	pl.title('Plot input vs predicted. avd m=%f, avg R^2=%f'%(avg_m,avg_r2))
	pl.legend(loc='upper left')
	pl.savefig('../lysate_linear.png')
	pl.show()

def run_a450_data() : 
	# Load data from file 
	fname = "../data/A450_raw.dat"
	with open(fname,"r") as fin :
		data = fin.readlines()
		data = np.array([float(val.strip()) for val in data ])
	#pdb.set_trace('R')
	data = data.reshape((7,9),order='F')
	pure_a450 = data[:,0]
	lysate_a450 = data[:,1:]
	nPoints,nSamples = lysate_a450.shape
	
	###################################################################
	# Find a least squares fit to pure protein
	
	input_prot = np.array(map(lambda(x):1000./2**x,range(7)))
	A = np.vstack([input_prot,np.ones(nPoints)]).T
	y = pure_a450
	coeffs,res = np.linalg.lstsq(A,y)[0:2]
	m,c = coeffs
	r2 = 1-res/y.var()
	pl.figure()
	x = input_prot
	pl.plot(x,m*x+c,'--',label='Standard curve',linewidth=2)	
	pl.plot(x,y,'-o',label='Pure antigen')
	pl.legend(loc="best")
	pl.xlabel('Conc of input')
	pl.ylabel('A450 value')
	pl.title('A450 values vs Protein concentration')
	print 'Slope=%f,Intercept=%f for standard curve'%(m,c)
	m_std = m 
	
	#######################################################################
	# Plot each of the lsyate proteins
		
	rlist = []
	mlist = []
	clist = []
	input_prot = np.array(map(lambda(x):1200./2**x,range(7)))
#	
#	
#	for i in range(nSamples) :
#		A = np.vstack([input_prot, np.ones(nPoints)]).T
#		y = lysate_a450[:,i]
#		coeffs,res = np.linalg.lstsq(A,y)[0:2]
#		m,c = coeffs
#		r2 = 1. - res/y.var() # calc r2 coeff
#		rlist.append(r2)
#		x = input_prot	
#		pl.plot(input_prot,y,label='lysate'+str(i+1))
#		#pl.plot(x,m*x+c,'--',label='lysate'+str(i+1))
#		mlist.append(m)
#		clist.append(c)
#	
#	pl.legend(loc="best")
#	#pl.show()
	
	#######################################################################
	# Plot Error Bars on the mean of the Lysate protein and compare with
	# standard curve
	
	x = lysate_a450.mean(axis=1)
	std = lysate_a450.std(axis=1)*1.5
	
	# Fit a linear equation to the average curve
	A = np.vstack([input_prot,np.ones(nPoints)]).T
	y = x
	coeffs,res = np.linalg.lstsq(A,y)[0:2]
	m,c = coeffs
	r2 = 1. - res/y.var()
	
	# Plot the Lysate Curves
	pl.plot(input_prot,m*input_prot+c,'r--',linewidth=2,label='Linear Fit')
	pl.errorbar(input_prot,x,fmt = 'o-',yerr=std,
	label="Avg Lysate curve",color='m')
	pl.legend(loc="best")
	pl.xlim([0,1300])
	pl.savefig('../lysate_linear.png')
	pl.show()
	print 'Slope=%f,Intercept=%f for Avg Lysate Curve'%(m,c)
	print 'Correction factor %f'%(m/m_std)
	print 'r2 value is %f' % (r2)	

def plot_lysate_proteins() : 
	# Load data from file 
	fname = "../data/A450_raw.dat"
	with open(fname,"r") as fin :
		data = fin.readlines()
		data = np.array([float(val.strip()) for val in data ])
	#pdb.set_trace('R')
	data = data.reshape((7,9),order='F')
	pure_a450 = data[:,0]
	lysate_a450 = data[:,1:]
	nPoints,nSamples = lysate_a450.shape
	

	#######################################################################
	# Plot each of the lsyate proteins
		
	rlist = []
	mlist = []
	clist = []
	input_prot = np.array(map(lambda(x):1200./2**x,range(7)))
	
	pl.figure()
	ax = pl.gca()
	ax.set_color_cycle(['r','g','b','c','y','k','orange','pink'])
	pl.title('Plot each of the individual lysate curves');
	for i in range(nSamples) :
		A = np.vstack([input_prot, np.ones(nPoints)]).T
		y = lysate_a450[:,i]
		coeffs,res = np.linalg.lstsq(A,y)[0:2]
		m,c = coeffs
		r2 = 1. - res/y.var() # calc r2 coeff
		rlist.append(r2)
		x = input_prot	
		pl.plot(input_prot,y,'--x',label='lysate'+str(i+1))
		#pl.plot(x,m*x+c,'--',label='lysate'+str(i+1))
		mlist.append(m)
		clist.append(c)
	
	x = lysate_a450.mean(axis=1)
	std = lysate_a450.std(axis=1)*1.5
	pl.errorbar(input_prot,x,fmt = 'o-',yerr=std,
	label="Avg Lysate curve",color='m',linewidth=3)
	
	
	pl.legend(loc="upper left")
	pl.xlim((0,1300))
	pl.xlabel('Concentration of mixture in ug/ml')
	pl.ylabel('A450 readings')
	pl.savefig('../lysate_only_linear.png')
	pl.show()
	
def back_predict() : 
	# Load data from file 
	fname = "../data/A450_raw.dat"
	with open(fname,"r") as fin :
		data = fin.readlines()
		data = np.array([float(val.strip()) for val in data ])
	#pdb.set_trace('R')
	data = data.reshape((7,9),order='F')
	pure_a450 = data[:,0]
	lysate_a450 = data[:,1:]
	nPoints,nSamples = lysate_a450.shape
	x = lysate_a450.mean(axis=1)
	lin = map(pred_linear,x)
	gokhale = map(pred_gokhale,x)
	print 'mean a450 - ', x
	print 'pure a450 - ', pure_a450
	print 'back pred linear - ', lin
	print 'back pred gokhake - ', gokhale
	
	# Calculate the factors
	def calc_facs(x) :		
		ret = map(lambda(pair) :(0.+pair[0])/pair[1],zip(x[0:-1],x[1:]))
		return ret	 
				
	fac_avg_lys = calc_facs(x-0.21) 
	fac_pure =  calc_facs(pure_a450-0.21)
	fac_back_lin = calc_facs(lin)
	fac_back_gokh = calc_facs(gokhale)

	print 'factors avg lysate', fac_avg_lys
	print 'factors pure prot', fac_pure
	print 'factors back-pred linear ', fac_back_lin
	print 'factors back-pred gokh', fac_back_gokh

def pred_linear(x) :
	return (x-0.28)/0.003144

def pred_gokhale(x) : 
	return 971.*(-6.064/(x-6.05)-1.)**(1./1.19)


#######################################################################
# Main Function

if __name__ == '__main__' : 
	#run_pred_data()
	run_a450_data()
	#plot_lysate_proteins()
	#back_predict()
