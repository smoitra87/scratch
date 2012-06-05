"""
Reads from edge files to draw edges on the GPCR structure

"""

import os,sys

import pymol
pymol.finish_launching()
from pymol import cmd

import glob;


DATA_DIR='/home/enzyme2012/Downloads'
edgef = '31-Aug-2011-edges.dat'
edgepath = os.path.join(DATA_DIR,edgef);
outfp = os.path.join(DATA_DIR,os.path.splitext(edgef)[0]+'.png')


#----------------------------------------------------------------------
# Draw Edges

# Clear previous stuff
cmd.delete('all');

# Load pdb
pdbfile = os.path.join(DATA_DIR,'3H4E.pdb');
cmd.load(pdbfile)

# prettify
cmd.hide('all')
cmd.show('ribbon','3H4E and chain A')
cmd.bg_color('white')


cmd.spectrum(palette = 'green_red', selection = '3H4E and chain A')
#cmd.select('retinal','3H4E and het and chain A and resn ret')
#cmd.show('spheres','retinal')
#cmd.color('magenta','retinal')

# constants
cutoff = 2

# Load the edges from file
with open(edgepath,'r') as fin : 
    data = fin.readlines();
edges = [line.strip().split() for line in data]


for n,e in  enumerate(edges) : 
    t = cmd.dist('dist'+str(n),'3H4E//A/'+e[0]+'/CA',\
		'3H4E//A/'+e[1]+'/CA')

    if t < cutoff  : 
        cmd.delete('dist'+str(n)) 
    else : 
        cmd.color('blue','dist'+str(n))
        cmd.hide('labels','dist'+str(n))
        cmd.show('spheres','3H4E//A/'+e[0]+'/CA')
        cmd.show('spheres','3H4E//A/'+e[1]+'/CA')
        cmd.color('yellow','3H4E//A/'+e[0]+'/CA')
        cmd.color('yellow','3H4E//A/'+e[1]+'/CA')

cmd.set('dash_radius','0.2');
cmd.set('dash_gap','0.0');
cmd.set('sphere_scale','0.3')
#cmd.set('sphere_scale','0.8','retinal');
cmd.ray()
print('*'*5+'Image:%s'%os.path.abspath(outfp)+'*'*5)
cmd.png(os.path.abspath(outfp))

print '-------Completed Call--------';


