from chomp_setup import *
from operator import mul
import numpy
import sys
import itertools


def init_poselibrary(r2vs):
    """Given a dictionary that maps residue IDs to vertex IDs, create a matching PoseLibrary for combinatorial optimization"""
    numblocks = len(r2vs)
    pl = PoseLibrary(numblocks)
    for i,r in enumerate(r2vs.keys()):
        pl.SetIDIndex(r2vs[r][0]) ## The first ID for this residue
        pl.GeneratePoseIDs(i, len(r2vs[r]))
    pl.dir = pl.DimensionIDRange
    pl.b2vs = dict( (b, range(pl.dir(b)[0], pl.dir(b)[-1]+1)) \
				for b in range(pl.NumDimensions()) )
    return pl

def init_eg(S, rl, n) : 
    ri = RotamerIterationMap(rl)
 
    eg = EnergyGraph()
    energy_function.FillEnergyGraph(rl, n, ri, eg)
 
    rl.dir = rl.DimensionIDRange
    rl.r2vs = dict( (S[b].ID, range(rl.dir(b)[0], rl.dir(b)[-1]+1)) for b in range(rl.NumDimensions()) )

    eg.r2vs = rl.r2vs
    eg.v2r = {}
    for r,vs in eg.r2vs.items():
        for v in vs: eg.v2r[v] = r
    eg.pl = init_poselibrary(eg.r2vs)
    eg.searchsize = reduce(mul, [len(x) for x in eg.r2vs.values()])
 
    return eg


def goldstein_singles_round(eg,target,taboo,verbose=False):
    """Try to eliminate rotamers from the target residue ID"""
    before = time()
    res2rots = eg.r2vs
    delete = set()
    possibilities = [v for v in res2rots[target] if v not in taboo]
 
 
    for v in possibilities: # Try to eliminate rotamer v
        if verbose: print '\n\nTrying to eliminate',v
        partners = set([eg.v2r[p] for p in eg.GetEdgeDestinationIDs(v,0.1)])
        for w in res2rots[target]:  # Through comparison to selected rotamers, w
            if w==v: continue
            if w in taboo: continue
            if verbose: print 'Through comparison with',w
            X = eg.GetVertexEnergy(v) - eg.GetVertexEnergy(w) #Single body energy difference
            if verbose: print 'onebody %d - onebody %d = %.2f' % (v,w,X)
            allpartners = partners.copy()
            allpartners.update( set([eg.v2r[p] for p in eg.GetEdgeDestinationIDs(w,0.1)]) )
            for p in allpartners:
                if verbose: print 'Considering interactions with partner',p,res2rots[p]
                alternatives = []
                best_imbalance = 0
                for u in res2rots[p]:
                    if u in taboo: continue ## If using the same taboo set for different target residues
                    diff = 0
                    try: diff += eg.GetEdgeEnergy(v,u)
                    except RuntimeError: pass
                    try: diff -= eg.GetEdgeEnergy(w,u)
                    except RuntimeError: pass
                    alternatives.append(diff)
                try:
                    Y = min(alternatives)
                    if verbose: print 'Considered %d alternative(s) for %d. Found minimum energy imbalance for %d (relative to %d) of %.2f' % (len(alternatives),p,v,w,Y)
                    X += Y
                except ValueError: pass
            if X>0:
                delete.add(v)
                taboo.add(v)
                #print 'Vertex %d is always better than %d ================================================================' % (w,v)
                if verbose: print 'Vertex %d is always better than %d (%.2f) ================================================================' % (w,v,X)
                break
            else:
                if verbose: print 'Vertex %d not necessarily better than %d (%.2f)================================================================' % (w,v,X)
    if verbose: print 'goldstein_singles_round: %.2f seconds to reduce %d choices to %d for %d' % (time()-before,len(possibilities), len(possibilities) - len(delete), target)
    return delete

if __name__ == '__main__' :
	S = NewSystem('data/1edmBH.pdb')

	generous_cutoffs = numpy.array([100]*400).reshape(20,20)
	nbmap = NeighborMap(S, generous_cutoffs)

	rl = RotamerLibrary(S)
	rg = RotamerGenerator(nbmap, dunbrack_lib)
	rl.GenerateRotamers(rg)
	
	eg = init_eg(S,rl,nbmap)

	# Write the energies to file
	res2rots = eg.r2vs
	res_list = S.GetResidueIDs()
	rots2res = eg.v2r

	outdir = 'out_dee'
	if not os.path.exists(outdir) :
		os.mkdir(outdir)		

	# Write out metadata
	with open(os.path.join(outdir,'metadata.dat'),'w') as fout :  
		fout.write("nResidues:{}\n".format(S.size))
		fout.write("Resid nRots:\n")
		for i in range(S.size) :
			fout.write("{0} {1}\n".format(i+1,\
				len(rl.DimensionIDRange(i))))
	
	# Write out vertex energies
	for resid in range(S.size) :
		with open(os.path.join(outdir,'Res-%d.energy'%(resid+1)),'w') \
				as fout: 
			for rotID in res2rots[S[resid].ID] : 
				fout.write("%f\n"%eg.GetVertexEnergy(rotID))

	# Write out edge energies 
	for r1,r2 in itertools.product(range(S.size),range(S.size)) : 
		with open(os.path.join(outdir,\
				'Edge-%d-%d.energy'%(r1+1,r2+1)),'w') as fout : 
			for rotID1 in res2rots[S[r1].ID] :
				for rotID2 in res2rots[S[r2].ID] : 
					try : 
						e = eg.GetEdgeEnergy(rotID1,rotID2)
						fout.write("{} ".format(e))
					except RuntimeError as e : 
						if 'FindEdge' not in e.message : 
							print(e)
							sys.exit(1)
						else : 
							fout.write("0.0 ")		
				fout.write("\n")
