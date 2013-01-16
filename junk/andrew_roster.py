with open('roster.txt') as fin : 
	lines = [line.split(' ')[-1] for line in fin.readlines() if line!='\n']

with open('roster_andrew.txt','w') as fout : 
	for line in lines : 
		fout.write(line)
