""" 
Testing my own scipy code
Integrate a function
y = f(x) = x^2+3

"""

from scipy.integrate import ode
import numpy as np
import pylab as pl

"""
 y[0] is x, y[1] is y
dy/dt = x
dx/dt = const
"""
y0,t0 = [1,1],0
def dy(t,y,arg1) : 
	return [arg1,y[0]]

r = ode(dy).set_integrator('vode',method='bdf',order=15)
r.set_initial_value(y0,t0).set_f_params(1.0)

t1 = 5
dt = 0.5

t = [t0]
y = [y0]

while r.successful()  and r.t < t1 : 
	r.integrate(r.t+dt)
	print r.t,r.y
	t.append(r.t)
	y.append(r.y)


pl.plot(t,y,'-o')
pl.xlabel('Time')
pl.ylabel('y,x')
pl.title('Plot of y,x vs t ')
pl.show()
