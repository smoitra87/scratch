"""
This program takes in an msa in the fasta format and returns an msa that
has it's columns stripped if those columns are low entropy columns. It also returns a mapping between columns between the new stripped msa and
the original msa

INPUT:
	foo.fasta
OUTPUT:
	foo_stripped.fasta
	foo_map.dat

foo_map.dat has 2 columns.
Col 1 - col id in stripped msa
Col 2

""
