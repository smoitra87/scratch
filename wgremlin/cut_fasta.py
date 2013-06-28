""" Convert Fasta to smaller size"""

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import generic_protein
import os,sys

CUT_LEN=20


if __name__ == '__main__'  : 
	fn = sys.argv[1]

	# Do file checks
	assert os.path.exists(fn) 
	root,ext = os.path.splitext(fn)
	assert ext in ('.fasta','.fas','.FAS','.FASTA')


	for seqr in SeqIO.parse(fn,'fasta') : 
		seqid = seqr.id
		seq  = seqr.seq
		seq = seq[:CUT_LEN] 
		# Write out fasta to new file
		sys.stdout.write(">>{}\n".format(seqid))
		sys.stdout.write("{}\n".format(seq))	
