""" Convert Fasta to .msa """

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import generic_protein
import os,sys


if __name__ == '__main__'  : 
	fnames = sys.argv[1:]

 	for fn in fnames : 
		# Do file checks
		assert os.path.exists(fn) 
		root,ext = os.path.splitext(fn)
		assert ext in ('.fasta','.fas','.FAS','.FASTA')


		with open(root+'.msa','w') as fout : 
			for seqr in SeqIO.parse(fn,'fasta') : 
				seqid = seqr.id
				seq  = seqr.seq
				# Write out files to new file
				fout.write("{} {}\n".format(seqid,seq))	
