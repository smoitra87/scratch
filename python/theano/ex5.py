#! /usr/bin/env python

from theano import tensor as T
from theano.ifelse import ifelse
from theano import function,shared

a,b,c = T.scalars(*'abc')
d = a+b
e = d+c

