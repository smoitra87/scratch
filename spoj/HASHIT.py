#! /usr/bin/env python
import sys

def hash(k) : 
	return (19*sum(map(lambda(x,y):ord(y)*(x+1),enumerate(k))))%101

def print_table(table) : 
	cnt,out = 0,""
	for idx,e in enumerate(table) : 
		if e != 0 : 
			out+=str(idx)+":"+e+"\n"
			cnt +=1
	sys.stderr.write(str(cnt)+"\n")
	sys.stderr.write(out)


t = int(sys.stdin.readline())

for t_ in range(t) : 
	n1 = int(sys.stdin.readline())
	table = [0]*101
	for i_ in range(n1) : 
		cmd,key = sys.stdin.readline().rstrip().split(':')
		hkey = hash(key)
		if cmd[0] == 'A' : 
			candpos,found = -1,False
			for j in range(0,20) : 
				pos = (hkey +j*j + 23*j)%101
				if table[pos] == key :
					found=True
					break
				if table[pos] == 0 and candpos < 0:
					candpos = pos
			if(candpos>=0) and not found : 
				table[candpos] = key
		else : 
			for j in range(0,20) : 
				pos = (hkey +j*j + 23*j)%101
				if table[pos] == key : 
					table[pos] = 0
					break
#		sys.stderr.write(cmd+key+"\n")
#		print_table(table)
	cnt,out = 0,""
	for idx,e in enumerate(table) : 
		if e != 0 : 
			out+=str(idx)+":"+e+"\n"
			cnt +=1
	sys.stdout.write(str(cnt)+"\n")
	sys.stdout.write(out)
			
				
			
		
