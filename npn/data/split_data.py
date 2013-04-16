import os,sys,random

if __name__ == '__main__' : 
	fname = sys.argv[1]	
	with open(fname) as fin : 
		data = fin.readlines()
		data = [line.strip() for line in data]
	random.shuffle(data)
	n = len(data)
	train= data[:int(round(n*0.9))]
	test = data[int(round(n*0.9)):]

	froot,ext = os.path.splitext(fname)
	with open(froot+'_train'+ext,'w') as fout : 
		for line in train : fout.write(line+'\n')
	with open(froot+'_test'+ext,'w') as fout : 
		for line in test : fout.write(line+'\n')

	
