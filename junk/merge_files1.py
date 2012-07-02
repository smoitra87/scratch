"""
This program merges RZZZ.SP files
"""

import os,sys,glob
from operator import itemgetter

globstr = 'R*.SP'
root = 'R'

if __name__ == '__main__'  :
	fnames=  glob.glob(globstr)
	fnums = map(lambda x: x[0][len(root):],map(os.path.splitext,fnames))
	fnums = map(int,fnums)
	ftups =  sorted(zip(fnames,fnums),key=itemgetter(1))
	fhandles = [(open(fn,'r'),fnum) for fn,fnum in ftups]

	# Write out headers to new file

	#close file handles
	fhandles = [(fin.close(),fnum) for fin,fnum in fhandles]

	
