"""
Parses rows and displays in pymol
"""

import os,sys
import pymol
import re
import time

pymol.finish_launching()
from pymol import cmd


fname = sys.argv[1]

with open(fname) as fin : 
	lines = fin.readlines()

tuples_list = []
for line in  lines : 
	tuples_list.append((line.split()[0],line.split()[2:]))

#lines = [(line.split()[0],line.split()[2:]) for line in lines ]

row = ('ASD00280000',
 ['subtilis',
  'site,339,Lys@@range,251,257,loop@@site,316,Lys@@site,318,Arg@@site,317,Asn'])

site_line = row[1][1]
nums = re.findall('\d+',site_line)

nicks_nums = [13,127,29,45]

#----------------------------------------------------------------------
# Pymol specific code

cmd.load('ASD00250000_3.pdb')
cmd.dist('resi '+str(nicks_nums[0]),', resi '+str(nicks_nums[1]))



