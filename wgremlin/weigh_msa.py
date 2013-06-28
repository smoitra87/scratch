""" Takes in a msa file and generates the weighted copy"""


CUT_ALIGN=True # Cut the alignment short
ALIGN_LEN=20



import os,sys,random


if __name__ == '__main__' : 
	fn = sys.argv[1]

	root,ext = os.path.splitext(fn)
	assert ext in ('.msa','.MSA')

	with open(fn) as fin : 
		lines = fin.readlines() 

	
	wts = []
	with open(root+'_wt.msa','w') as fout: 
		for line in lines :

			wt = random.choice(range(1,100))
			wts.append(wt)
			seqid,seq = line.strip().split()

			if CUT_ALIGN : 
				seq = seq[:ALIGN_LEN]

			for i in range(wt)  :
				fout.write("{} {}\n".format(seqid,seq))


	with open(root+'.wt','w') as fout : 

		for wt in wts : 
			fout.write('{}\n'.format(wt))











