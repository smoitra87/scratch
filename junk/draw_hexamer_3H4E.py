"""
Reads from edge files to draw edges on the GPCR structure

"""

import os,sys

import pymol
pymol.finish_launching()
from pymol import cmd

import glob;
from itertools import combinations


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
cmd.show('cartoon','3H4E and chain A+B+C+D+E+F')
cmd.bg_color('white')


#cmd.spectrum(palette = 'green_red', selection = '3H4E and chain A')
cmd.util.cbc()
#cmd.select('retinal','3H4E and het and chain A and resn ret')
#cmd.show('spheres','retinal')
#cmd.color('magenta','retinal')

# Set the view for monomer
#cmd.set_view(\
#    '-0.912057340,   -0.295883119,   -0.283901036,\
#     0.399889141,   -0.795006156,   -0.456119299,\
#    -0.090745762,   -0.529538393,    0.843419492,\
#     0.000087761,   -0.000581503, -183.590560913,\
#     8.321296692,  -66.967765808,  -33.590000153,\
#   -36.799331665,  403.937011719,  -20.000000000' )

# Set the view from top
cmd.set_view (\
     '0.455506235,   -0.389297336,    0.800600052,\
    -0.483749777,    0.646710277,    0.589702904,\
    -0.747330904,   -0.655901074,    0.106259122,\
     0.000163019,    0.000150129, -316.468078613,\
   -37.810100555,  -63.827388763,  -22.882722855,\
   221.616317749,  411.317382812,  -20.000000000' )

# Set the view from the bottom
#cmd.set_view (\
#     0.509821594,    0.429360747,   -0.745473742,\
#    -0.444633365,   -0.610314071,   -0.655602694,\
#    -0.736464798,    0.665700138,   -0.120242476,\
#     0.000000000,    0.000000000, -294.413665771,\
#   -13.488616943,  -48.363307953,  -22.056068420,\
#   232.117980957,  356.709350586,  -20.000000000 )


# constants
cutoff = 2

# Load the edges from file
with open(edgepath,'r') as fin : 
    data = fin.readlines();
edges = [line.strip().split() for line in data]

chains = ['A','B','C','D','E','F']
comb_chains = combinations(chains,2)

for n,e in  enumerate(edges) : 
    for ch in chains : 
       t = cmd.dist('dist'+str(n),'3H4E//'+ch+'/'+e[0]+'/CA',\
		'3H4E//'+ch+'/'+e[1]+'/CA')

       if t < cutoff  : 
           cmd.delete('dist'+str(n)) 
       else : 
           cmd.color('blue','dist'+str(n))
           cmd.hide('labels','dist'+str(n))
           cmd.show('spheres','3H4E//'+ch+'/'+e[0]+'/CA')
           cmd.show('spheres','3H4E//'+ch+'/'+e[1]+'/CA')
           cmd.color('yellow','3H4E//'+ch+'/'+e[0]+'/CA')
           cmd.color('yellow','3H4E//'+ch+'/'+e[1]+'/CA')

cmd.set('dash_radius','0.2');
cmd.set('dash_gap','0.0');
cmd.set('sphere_scale','0.3')
#cmd.set('sphere_scale','0.8','retinal');
#cmd.ray()
print('*'*5+'Image:%s'%os.path.abspath(outfp)+'*'*5)
#cmd.png(os.path.abspath(outfp))

print '-------Completed Call--------';


