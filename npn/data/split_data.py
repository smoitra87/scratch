import os,sys,random

if __name__ == '__main__' : 
	fname = sys.argv[1]	
	with open(fname) as fin : 
		data = fin.readlines()
	random.shuffle(data)
	n = len(data)
	train= data[:int(round(n*0.9))]
	test = data[int(round(n*0.9)):]

	froot,ext = os.path.splitext(fname)
	with open(froot+'_train'+ext,'w') as fout : 
		fout.writelines(train)
	with open(froot+'_test'+ext,'w') as fout : 
		fout.writelines(test)

	
	

	
