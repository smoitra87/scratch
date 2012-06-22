"""

This is a quick script that creates the MSA for Hexokinase 1

"""


import os,sys

import Bio
from Bio import SeqIO, AlignIO,  SeqRecord, Alphabet
from Bio.Seq import Seq

from operator import itemgetter


#----------------------------------------------------------------------
# Set some constants and other thigns

DATA_DIR="data"
hexfn = "PF00349_full.fasta"
hexfp = os.path.join(DATA_DIR,hexfn)
canon_seqid="HXK1_HUMAN/16-221" # id of canonical hexokinase sequence
outhexfn = "Hexokinase.fasta"
outhexfp = os.path.join(DATA_DIR,outhexfn)
gap_cutoff = 0.5 # remove all sequences with more than 50% gap

#----------------------------------------------------------------------
# Load the msa file and then process then process the columsn

aln = AlignIO.read(open(hexfp),"fasta",alphabet=Alphabet.IUPAC.protein)

# find the HKX1_HUMAN sequence record
canon_seqr = filter(lambda s:s.id==canon_seqid,aln)[0]
canon_seq = canon_seqr.seq.tostring()

# Find the columns that have aa for HXK1_HUMAN
pos_aa = [] # list of aa positions
aln2 = None

for idx,aa in enumerate(canon_seq) :
	if aa != '-' :  
		pos_aa.append(idx)

# Filter columns that dont correspond to the canonical sequence
for seqr in aln : 
	s = seqr.seq
	s_new = "".join(map(itemgetter(1),filter(lambda t:t[0] in pos_aa,\
		enumerate(s))))
	s_new = s_new.replace('-','.')
	seqr.seq = Seq(s_new,alphabet=Alphabet.IUPAC.protein)

msa_hex= []
# Remove sequences with too many gaps
for seqr in aln : 
	if (0.0+seqr.seq.count('.'))/len(seqr.seq) > gap_cutoff : 
		continue 
	else : 
		msa_hex.append(seqr)

#----------------------------------------------------------------------
# Write out new alignment

print("Hexokinase MSA has %d rows and %d columns"%\
	(len(msa_hex),len(msa_hex[0])))

SeqIO.write(msa_hex,outhexfp,"fasta")

