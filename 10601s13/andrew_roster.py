""" Compares the different rosters"""

import itertools

#rosterdict = {
#'roster_jan13' : 'roster.txt',
#'roster_jan16' : 'roster_jan16.txt',
#'roster_wait_jan16' : 'roster_wait_jan16.txt',
#'wait_22_refer' : 'wait_22_refer.txt',
#'wait_22' : 'wait_22.txt',
#'roster_jan28' : 'roster_jan28.txt'
#}
#
rosterdict = {
'roster_hw5' : 'studs.dat',
'roster_exam' : 'bla.dat'

}




def readroster(fpath) : 
	""" Reads a roster file and returns andrew ids """
	with open(fpath) as fin : 
		lines = [line.split(' ')[-1].strip() for line in \
			fin.readlines() if line!='\n']
	return lines

def readroster_wait(fpath) : 
	""" Reads a roster file in waiting list format """
	with open(fpath) as fin : 
		lines = [line[56:].split()[0] for line in fin.readlines()]
	return lines

def compare_ids(id1_name,id1,id2_name,id2) : 
	""" Compares two list of ids"""
	print("*"*15+"Comparing {0} and {1} ".format(id1_name,id2_name)+\
		"*"*15)
	print('{0} and {1} : {3} : {2}'.format(id1_name,id2_name,\
			set(id1).intersection(id2),len(set(id1).intersection(id2))))
	print('{0} - {1} : {3} : {2}'.format(id1_name,id2_name,\
			set(id1).difference(id2),len(set(id1).difference(id2))))
	print('{1} - {0} : {3} : {2}'.format(id1_name,id2_name,\
			set(id2).difference(id1),len(set(id2).difference(id1))))

def write_andrewids(ids,fname) : 
	""" Write out a list of andrew ids"""
	with open(fname,'w') as fout : 
		for id in ids: 
			fout.write(id+'@andrew.cmu.edu\n')
def write_ids(ids,fname) : 
	""" Write out a list of andrew ids"""
	with open(fname,'w') as fout : 
		for id in ids: 
			fout.write(id+"\n")



if __name__ == '__main__' : 
	ids = {}
	for key in rosterdict.keys() : 
		if 'wait' in key : 
			ids[key] = readroster_wait(rosterdict[key])
		else : 
			ids[key] = readroster(rosterdict[key])

	for id1,id2 in itertools.combinations(rosterdict.keys(),2) :
		compare_ids(id1,ids[id1],id2,ids[id2])

	write_andrewids(set(ids['roster_jan16']).\
			difference(ids['roster_jan13']),'new_16.ids')
	write_andrewids(ids['roster_wait_jan16'],'wait_16.ids')
	write_ids(ids['roster_jan16'],'ids_jan16.ids')
	write_ids(ids['wait_22_refer'],'ids_refer_22.ids')
	write_andrewids(set(ids['wait_22']).\
			difference(ids['wait_22_refer']),'ids_nonrefer_22.ids')
	write_andrewids(ids['roster_jan28'],'ids_jan28.ids')
