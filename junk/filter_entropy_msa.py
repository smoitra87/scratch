#! /usr/bin/env python

"""
This program takes in an msa in the fasta format and returns an msa that
has it's columns stripped if those columns are low entropy columns. It also returns a mapping between columns between the new stripped msa and
the original msa

Usage: filter_entropy_msa.py [options] FASTAFILE

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -v, --viz             visualize entropy histogram
  -c CUTOFF, --entcutoff=CUTOFF
                        cutoff value for enrtropy
foo_map.dat has 2 columns.
Col 1 - col id in stripped msa
Col 2 - col id in original msa

"""

import os, sys
import numpy as np
import pylab as pl

from Bio import AlignIO, SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import Alphabet

from optparse import OptionParser
from operator import itemgetter

#----------------------------------------------------------------------
# Define constants, file paths and other things

ENTROPY_CUTOFF=0.05

#----------------------------------------------------------------------
# Do Entropy calculations and strip

def calc_ent_aa(aln) :
	""" Calculate the entropy for each amino acid position"""
	info_cols = [] # Non conserved columns
	for col_id in range(aln.get_alignment_length()) :
		col = aln.get_column(col_id)
		ftab = {} # Freq table
		for c in col :
			ftab[c] = ftab.get(c,0) + 1
		counts = ftab.values()
		sum_c = sum(counts)
		p = map(lambda x : (0.0+x)/sum_c,counts) # probabilities
		e = -reduce(lambda x,y:x+y,map(lambda t:t[0]*t[1],\
			zip(p,np.log(p))))
		info_cols.append(e)
	return info_cols


if __name__ == '__main__' : 

	#------------------------------------------------------------------
	# Define the options parser
	usage="%prog [options] FASTAFILE"
	parser = OptionParser(usage=usage,version="%prog 0.1")
#	parser.add_option("-f","--file",dest="fname",\
#		help="fasta file to strip",metavar="FASTA")
	parser.add_option("-v","--viz",dest="viz",\
		help="visualize entropy histogram",action="store_true",\
		default=False)
	parser.add_option("-c","--entcutoff",dest="entcutoff",\
		help="cutoff value for enrtropy",metavar="CUTOFF",\
		type="float",nargs=1,default=ENTROPY_CUTOFF)

	(options,args) = parser.parse_args()
	
	if len(args) != 1 :
		parser.error("incorrect number of arguments")
	else : 
		fpath = args[0]
		if not os.path.exists(fpath) :
			raise IOError("File %s not found"%(fpath))

	print("Stripping columns from %s"%(args[0]))

	#------------------------------------------------------------------
	# Read columns and filter them according to entropy

	aln = AlignIO.read(open(fpath),"fasta")
	print(repr(aln))
	info_cols = calc_ent_aa(aln)
	

	# Make a histogram of entropy for each column
	if options.viz :
		pl.figure()	
		pl.title("Hist plot of entropy for the aa columns")
		pl.xlabel("Entropy Values")
		pl.hist(info_cols,bins=30)
		pl.axvline(x=options.entcutoff,color="black",linewidth=2,\
			linestyle="dashed",label="cutoff")
		pl.legend()
		#pl.show()
		imgfname = os.path.splitext(fpath)[0]+'_entropy.png'
		pl.savefig(imgfname)
		pl.close()


	# Find columns that satisfy cutoff 
	cols = np.where(np.array(info_cols)>options.entcutoff)[0]
	cols_remove = np.where(np.array(info_cols)<=options.entcutoff)[0]

	# Filter columns that dont correspond to the canonical sequence
	for seqr in aln : 
		s = seqr.seq
		s_new = "".join(map(itemgetter(1),\
		filter(lambda t:t[0] in cols,enumerate(s))))
		s_new = s_new.replace('-','.')
		seqr.seq = Seq(s_new,alphabet=Alphabet.IUPAC.protein)

	print("%d Columns were stripped"%(len(cols_remove)))
	outfpath = os.path.splitext(fpath)[0]+"_stripped.fasta"
	print("Writing stripped Fasta file to %s"%(outfpath))
	SeqIO.write(aln,outfpath,"fasta")

	# Create mapping file
	mapping = map(lambda t:(t[0]+1,t[1]+1),enumerate(cols))
	mappingfpath = os.path.splitext(fpath)[0]+"_mapping.dat"
	with open(mappingfpath,'w') as fout : 
		for elem in mapping : 
			fout.write("%d %d\n"%(elem[0],elem[1]))
	


	
	


	
