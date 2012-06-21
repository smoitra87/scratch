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

from optparse import OptionParser


#----------------------------------------------------------------------
# Define constants, file paths and other things

ENTROPY_CUTOFF=0.1


#----------------------------------------------------------------------
# Read columns and filter them according to entropy

if __name__ == '__main__' : 

	# Define the options parser
	usage="%prog [options] FASTAFILE"
	parser = OptionParser(usage=usage,version="0.1")
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

	print("Stripping columns from %s"%(args[0]))
	
