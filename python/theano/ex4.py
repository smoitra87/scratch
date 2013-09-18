#! /usr/bin/env python

# Using shared variables and overriding the values of shared variables


import theano
from theano import tensor as T
from theano import shared,function


state = shared(0)
inc = T.iscalar('inc')

out = 2*state + inc
foo = T.scalar(dtype=state.dtype)

withshared = function(inputs=[inc],outputs=out)
skipshared = function(inputs=[inc,foo],outputs=out,givens=[(state,foo)])

print state.get_value()
print withshared(2)
print skipshared(5,1)
print state.get_value()
