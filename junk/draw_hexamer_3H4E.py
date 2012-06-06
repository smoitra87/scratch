"""
Reads from edge files to draw edges on the GPCR structure

"""

import os,sys

import pymol
pymol.finish_launching()
from pymol import cmd

import glob;
import itertools 
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

# Set the view from top
cmd.set_view (\
     '0.455506235,   -0.389297336,    0.800600052,\
    -0.483749777,    0.646710277,    0.589702904,\
    -0.747330904,   -0.655901074,    0.106259122,\
     0.000163019,    0.000150129, -316.468078613,\
   -37.810100555,  -63.827388763,  -22.882722855,\
   221.616317749,  411.317382812,  -20.000000000' )



# constants
cutoff = 2

# Load the edges from file
with open(edgepath,'r') as fin : 
    data = fin.readlines();
edges = [line.strip().split() for line in data]

chains = ['A','B','C','D','E','F']



for n,e in  enumerate(edges) : 
    for ch in chains : 
       t = cmd.dist('dist'+ch+str(n),'3H4E//'+ch+'/'+e[0]+'/CA',\
		'3H4E//'+ch+'/'+e[1]+'/CA')

       if t < cutoff  : 
           cmd.delete('dist'+ch+str(n)) 
       else : 
           cmd.color('blue','dist'+ch+str(n))
           cmd.hide('labels','dist'+ch+str(n))
           cmd.show('spheres','3H4E//'+ch+'/'+e[0]+'/CA')
           cmd.show('spheres','3H4E//'+ch+'/'+e[1]+'/CA')
           cmd.color('yellow','3H4E//'+ch+'/'+e[0]+'/CA')
           cmd.color('yellow','3H4E//'+ch+'/'+e[1]+'/CA')

# Create a set of residues
set_res = []
for e_tup in edges : 
	set_res.extend(e_tup)
set_res = set(set_res)

for ch,resi in itertools.product(chains,set_res) : 
	cmd.label('3H4E//'+ch+'/'+resi+'/CA','"%s%s"%(resn,resi)')

cmd.set('dash_radius','0.2');
cmd.set('dash_gap','0.0');
cmd.set('sphere_scale','0.3')
#cmd.set('sphere_scale','0.8','retinal');
#cmd.ray()
outfp = os.path.join(DATA_DIR,os.path.splitext(edgef)[0]+'_hex_top.png')
print('*'*5+'Image:%s'%os.path.abspath(outfp)+'*'*5)
cmd.png(os.path.abspath(outfp))
print('-----Finished drawing from top -----')

# Set the view from the bottom
cmd.set_view (\
    '-0.062551118,    0.668488383,   -0.741087615,\
     0.326947540,   -0.687838376,   -0.648059845,\
    -0.942967236,   -0.282835305,   -0.175534144,\
     0.000000000,    0.000000000, -294.413665771,\
   -13.488616943,  -48.363307953,  -22.056068420,\
   232.117980957,  356.709350586,  -20.000000000' )
#cmd.ray()
outfp = os.path.join(DATA_DIR,os.path.splitext(edgef)[0]+'_hex_bottom.png')
print('*'*5+'Image:%s'%os.path.abspath(outfp)+'*'*5)
cmd.png(os.path.abspath(outfp))

print('-----Finished drawing from bottom -----')
#
##---------------------------------------------------------------
## Draw edges across

# Delete the previous edges
cmd.delete('dist*')

for n,e in  enumerate(edges) : # For each edge
    for ch1,ch2 in  combinations(chains,2) : # For each chain
       for ii in range(2) : # Draw edges in both directions
           if ii %2 == 1:
               ch1,ch2 = ch2,ch1
       	   t = cmd.dist('dist'+ch1+ch2+str(n),'3H4E//'+ch1+'/'+e[0]+'/CA',\
       		'3H4E//'+ch2+'/'+e[1]+'/CA')
           #print('dist'+ch1+ch2+str(n))       		
       	   if t < cutoff : 
               cmd.delete('dist'+ch1+ch2+str(n))
           else : 
               cmd.color('blue','dist'+ch1+ch2+str(n))
               cmd.hide('labels','dist'+ch1+ch2+str(n))
               cmd.show('spheres','3H4E//'+ch1+'/'+e[0]+'/CA')
               cmd.show('spheres','3H4E//'+ch2+'/'+e[1]+'/CA')
               cmd.color('yellow','3H4E//'+ch1+'/'+e[0]+'/CA')
               cmd.color('yellow','3H4E//'+ch2+'/'+e[1]+'/CA')
    #print e
    
      
#cmd.ray()
outfp = os.path.join(DATA_DIR,os.path.splitext(edgef)[0]+'_hex_across.png')
print('*'*5+'Image:%s'%os.path.abspath(outfp)+'*'*5)
cmd.png(os.path.abspath(outfp))
print('-----Finished drawing from top -----')


print '-------Completed Call--------';


