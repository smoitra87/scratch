"""
Program for doing DEE pruning
"""

import numpy as np
from operator import itemgetter
from itertools import product
import pickle
from pdb import set_trace as stop

# Define some constaint
MAXVAL=1e100
MAX_E = 30
MIN_E = 0
N,R = 5,3 # Num aa and nrot/aa

class Protein(object) : 
	""" Describes a protein object"""
	def __init__(self,n,r) : 
		self.n = n
		self.r = r
		# Assign Energies
		self.Es = np.random.uniform(MIN_E,MAX_E,(n,r))
		self.Ep = np.zeros((n,n,r,r))		
		for i in range(n) : 
			for j in range(i+1,n) : 
				x = np.random.uniform(MIN_E,MAX_E,(r,r))
				self.Ep[i][j] = x 
				self.Ep[j][i] = x.T		

		self.rotSpace = []
		for i in range(n) : 
			self.rotSpace.append(range(r));

	def calc_Energy(self,conf) :
		""" Calculates Energy for a particular conformation"""
		E_unit = E_pair = 0
		Ep  = self.Ep
		Es = self.Es
		c = conf
		E_unit = np.sum(map(lambda(c):Es[c[0]][c[1]],enumerate(conf)))
		for i in range(len(conf)):
			for j in range(i+1,len(conf)) : 
				E_pair += Ep[i][j][conf[i]][conf[j]] 
		return E_unit + E_pair

class TestProtein(Protein) : 
	def __init__(self) : 
		super(TestProtein,self).__init__(3,3)
		self.Ep[1][2][1][0] = 1000
		self.Ep[1][2][1][1] = 1000
		self.Ep[1][2][1][2] = 1000
		self.Ep[2][1][0][1] = 1000
		self.Ep[2][1][1][1] = 1000
		self.Ep[2][1][2][1] = 1000

				

class SCPSolver(object) : 
	""" Solves the side chain placment problem"""
	def __init__(self,p):	
		self.p = p
		self.sched = self.sched1
		# Define rotameric space
		self.rotSpace = p.rotSpace

	def findmin_brute(self) : 
		""" Find min using brute force search """
		min_energy = MAXVAL
		for c in product(*self.rotSpace) : 
			if min_energy > p.calc_Energy(c) : 
				min_energy = p.calc_Energy(c)
				min_conf = c
		print("Min Energy is: {0}".format(min_energy))
		print("GMEC is {0}".format(min_conf))
		


	def Desmet_DEE(self)  :
		""" Execute the original Desmet DEE criteria"""
		# Complexity $O(n^2r^2)$
		n = self.p.n
		Es = self.p.Es
		Ep = self.p.Ep
		rotSpace = self.p.rotSpace

		elimRots = {}
		for i in range(n) :
			lhs = [0]*self.p.r
			rhs = [0]*self.p.r
			for r in rotSpace[i] :
				lhs[r] = rhs[r] = Es[i][r]
				for j in range(n) :
					if j == i : continue
					rspj = rotSpace[j]
					lhs[r] = lhs[r] + \
						min([Ep[i][j][r][s] for s in rspj])
					rhs[r] = rhs[r] + \
						max([Ep[i][j][r][s] for s in rspj])
			# Check filtering criteria
			for r in rotSpace[i] :
				for t in rotSpace[i] :
					if(lhs[r]>rhs[t]) :
						try :
							elimRots[i].append((r,t))
						except KeyError : 
							elimRots[i] = [(r,t)]
						break;
	
		# Eliminate the flagged rotamers
		for i in elimRots.keys() : 
			for r,t in elimRots[i] : 
				print("Rot{0} elim by Rot{1} in res{2}".format(r,t,i))
			removed = map(itemgetter(0),elimRots[i])
			rotSpace[i] = filter(lambda(x): x not in removed,\
								rotSpace[i])			

	
	def Desmet_DEE_pair(self)  : 
		""" Execute the pairs DEE criteria """
		# Complexity $O(n)$
		# Complexity $O(n^2r^2)$
		r = self.p.r
		n = self.p.n
		Es = self.p.Es
		Ep = self.p.Ep
		rotSpace = self.p.rotSpace

	def Goldstein_DEE(self) : 
		""" Execute the Goldstein singles DEE criteria """
		# Complexity $O(n^2r^3)$
		r = self.p.r
		n = self.p.n
		Es = self.p.Es
		Ep = self.p.Ep
		rotSpace = self.p.rotSpace

		elimRots = {}
		for i in range(n) :
			for r in rotSpace[i] :
				for t in rotSpace[i] : 
					if t == r :	continue
					
					X = Es[i][r] -Es[i][t]
					for j in range(n) :
						if j == i : continue
						rspj = rotSpace[j]
						Y = min([Ep[i][j][r][s]-Ep[i][j][t][s] \
								for s in rspj])
						X += Y
					if X > 0 : 
						try :
							elimRots[i].append((r,t))
						except KeyError : 
							elimRots[i] = [(r,t)]
						break;

		# Eliminate the flagged rotamers
		for i in elimRots.keys() : 
			for r,t in elimRots[i] : 
				print("Rot{0} elim by Rot{1} in res{2}".format(r,t,i))
			removed = map(itemgetter(0),elimRots[i])
			rotSpace[i] = filter(lambda(x): x not in removed,\
								rotSpace[i])			

	def Goldstein_DEE_pairself(self) : 
		""" Execute the pairs Goldstein DEE criteria"""
		# Complexity $O(n^3r^5)$
		pass

	def SimpleSplit_DEE(self) : 
		""" Prune search space using split DEE criteria"""
		n = self.p.n
		Es = self.p.Es
		Ep = self.p.Ep
		rotSpace = self.p.rotSpace

		elimRots = {}
		Y = np.zeros((n,self.p.r))
		for i in range(n) :
			for r in rotSpace[i] :
				elim_r = False # master flag to help breaking
				for t in rotSpace[i] : 
					if t == r :	continue
					for j in range(n) :
						if j == i : continue
						rspj = rotSpace[j]
						Y[j][t] = min([Ep[i][j][r][s]-Ep[i][j][t][s] \
								for s in rspj])
				for k in range(n) : 
					if i==k  : continue 
					elim = [False]*self.p.r
					for t in rotSpace[i] : 
						if t==r : continue
						X = Es[i][r] - Es[i][t]
						for j in range(n) : 
							if j == i or j==k : continue 
							X += Y[j][t]
						for v in rotSpace[k] : 
							if X + Ep[i][k][r][v] - Ep[i][k][t][v]> 0 : 
								elim[v] = True
					elim_all = reduce(lambda x,y:x and y,\
						[elim[v] for v in rotSpace[k]])
					if elim_all == True : 
						try :
							elimRots[i].append((r,k))
						except KeyError : 
							elimRots[i] = [(r,k)]
						elim_r = True 
						break
				if elim_r == True : break 	
	
		# Eliminate the flagged rotamers
		for i in elimRots.keys() : 
			for r,k in elimRots[i] : 
				print("Rot{0} elim by split{1} in res{2}".format(r,k,i))
			removed = map(itemgetter(0),elimRots[i])
			rotSpace[i] = filter(lambda(x): x not in removed,\
								rotSpace[i])			

	


	def _pspace(self)  :	
		""" Prints length of param space """
		return reduce(lambda x,y:x*y,map(len,self.rotSpace))

	def print_rotSpace(self) :
		""" Prints the rotamer space """
		print("-"*20+"Rotameric space"+"-"*20);
		print("Param space:{0}".format(self._pspace()))
		for i,rots in enumerate(self.rotSpace) : 
			print("{0}: {1}".format(i,rots))

	def sched1(self) :
		""" Execute the following schedule and print results """
	
		self.print_rotSpace()
		self.findmin_brute()
		print("-"*20+"Running Desmet DEE"+"-"*20)
		self.Desmet_DEE() 
		print("-"*20+"Running Desmet DEE"+"-"*20)
		self.Desmet_DEE() 
		print("-"*20+"Running Goldstein DEE"+"-"*20)
		self.Goldstein_DEE() 
		print("-"*20+"Running Simple Split DEE"+"-"*20)
		self.SimpleSplit_DEE() 
	
		self.print_rotSpace()
		self.findmin_brute()


	def solve(self)  :
		""" Call a schedule to solve the problem """
		self.sched1()



if __name__ == '__main__' : 
	# Initialize stuff
	p = Protein(N,R)
#	p = TestProtein()
#	with open('prot.pkl') as fin : 
#		p = pickle.load(fin)
	scp = SCPSolver(p) 
	scp.solve()





