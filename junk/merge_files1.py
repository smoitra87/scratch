"""
This program merges RZZZ.SP files
"""

import os,sys,glob
from operator import itemgetter
import re


globstr = '*.SP'
#root = 'R'
outfn = 'final_merged.csv'
skip_count = 86


if __name__ == '__main__'  :
	fnames=  glob.glob(globstr)
#	fnums = map(lambda x: x[0][len(root):],\
#		map(os.path.splitext,fnames))
	regex = re.compile('\d+')
	fnums = [regex.findall(fn)[0] for fn in fnames]
	
	fnums = map(int,fnums)
	ftups =  sorted(zip(fnames,fnums),key=itemgetter(1))
	fhandles = [(open(fn,'r'),fnum) for fn,fnum in ftups]

	# Skip lines
	for fin,fnum in fhandles :
		for i in range(skip_count) : fin.readline()	
	
	with open(outfn,'w') as outf : 
		# Write out headers
		outf.write(",")
		outf.write(",".join(map(str,sorted(fnums)))+"\n")
		
		# Start writing data

		# Get the data
		try :
			while True : 
				# Get the row name
				fin = fhandles[0][0]
				curr = fin.tell()
				line = fin.readline()
				rowval = line.split()[0]
				outf.write(rowval+",")
				fin.seek(curr)
		
				outf.write(\
				",".join([fin.readline().split()[1] \
					for fin,fnum in fhandles]))
				outf.write("\n")
		except IndexError : 
			pass

	#close file handles
	fhandles = [(fin.close(),fnum) for fin,fnum in fhandles]

	
