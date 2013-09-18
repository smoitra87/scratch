#! /usr/bin/env python

# Writing an incrementor and a decrementor using shared variables

import theano
from theano import tensor as T
from theano import function,shared

state = shared(0)
inc = T.iscalar('inc')

incrementor = function(inputs=[inc],outputs=state,updates=[(state,state+inc)])
decrementor = function(inputs=[inc],outputs=state,updates=[(state,state-inc)])

print state.get_value()
incrementor(1)
print state.get_value()
decrementor(2)
print(state.get_value())
state.set_value(10)
print state.get_value()
