"""
Program to accept multiple floats and print products or print max
"""

import argparse,sys

if __name__ == '__main__' : 
	parser = argparse.ArgumentParser(description="Multiplies integers",\
		prog="integer-multiplier")
	parser.add_argument("integers",type=int,nargs='+',metavar='INT')
	fmul = lambda l : reduce(lambda x,y : x*y,l)
	parser.add_argument('-m','--mul',dest='func',action="store_const",const=fmul,\
		default=max)
	args = parser.parse_args()
	print("Result is %d"%args.func(args.integers))
	

