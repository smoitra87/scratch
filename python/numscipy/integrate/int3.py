"""
Testing my own scipy code
for integration om Chou2006 diffeqns


"""

from scipy.integrate import ode
import numpy as np
import pylab as pl

ss_params = {
'alpha' : [12,8,3,2],
'beta' : [10,3,5,6],
'g' : [
	[0,0,-0.8,0],
	[0.5,0,0,0],
	[0,0.75,0,0],
	[0.5,0,0,0]
	],
'h' : [
	[0.5,0,0,0],
	[0,0.75,0,0],
	[0,0,0.5,0.2],
	[0,0,0,0.8]
]
}

y0,t0 = [1.4,2.7,1.2,0.4],0


def dy(t,y,ss) :
	slope = []
	for eqn in zip(ss['alpha'],ss['beta'],ss['g'],ss['h']) : 
		a,b,g,h = eqn
		expf = lambda(x) : x[0] ** x[1]
		mulf = lambda x,y  : x*y
		prod = a*reduce(mulf,map(expf,zip(y,g)))
		degrad = b*reduce(mulf,map(expf,zip(y,h))) 
		slope.append(prod-degrad)
	return slope	

r = ode(dy).set_integrator('vode',method='bdf',order=15)
r.set_initial_value(y0,t0).set_f_params(ss_params)

t_end,dt = 5,0.1
t,y = [t0],[y0]

while r.successful() and r.t < t_end : 
	r.integrate(r.t+dt)
	#print r.t,r.y
	t.append(r.t)
	y.append(r.y)

ax = pl.gca()
ax.set_color_cycle(['r','b','g','c'])
pl.plot(t,y,'.')
pl.xlabel('Time')
pl.ylabel('Concentration')
pl.title('Plot of Conc vs time')
pl.show()

