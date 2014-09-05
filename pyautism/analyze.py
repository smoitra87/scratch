import os,sys
import numpy as np
import matplotlib.pyplot as plt
import itertools as it
import random
from collections import defaultdict
from collections import Counter

ALPHABET="ACTG"
GENOME_LENGTH=int(30e3)
NUM_DENOVO=30
SEQERR_RATES=[10**i for i in range(-5,-1)]
SEQDEPTH_MEAN=40

def cumsum(it):
    """ Returns a generator that calculates the cumulative prob """
    total = 0.
    for x in it : 
        total += x
        yield total

def create_seqreads(mom,dad,denovo_flag):
    """Generate seqreads after consuming single nucleotides from
        mom and dad """
    seqdepth = np.random.poisson(lam=SEQDEPTH_MEAN)
    charMap = dict(zip(ALPHABET,range(len(ALPHABET))))

    # character multonimial p(A,C,T,G) ; \sum_{c\in Alphabet} p(c) = 1
    multinomial_prob = [0]*len(ALPHABET)
    for c in (mom,dad):
        multinomial_prob[charMap[c]] += 0.5

#    assert sum(multinomial_prob) == 1.
    seqreads = Counter((random.choice((mom,dad)) for _ in xrange(seqdepth)))

    if denovo_flag : 
        # Flip some character to some other 
        flip_source_positions = [charMap[c] for c in (mom,dad)] 
        flip_source_position = random.choice(flip_source_positions) 

        flip_target_positions =  \
           set(range(len(ALPHABET))).difference(flip_source_positions)
        flip_target_positions = list(flip_target_positions)
        flip_target_position = random.choice(flip_target_positions)

        multinomial_prob[flip_target_position] += 0.5
        multinomial_prob[flip_source_position] -= 0.5

#        assert sum(multinomial_prob) == 1.
        cum_prob = list(cumsum(multinomial_prob)) 
        sample_read = lambda u: ALPHABET[\
                next(i for (i,cp) in enumerate(cum_prob) if u < cp)\
                ]
        seqreads = Counter(\
                [sample_read(random.random()) for _ in xrange(seqdepth)]\
                )

    return seqreads

def gen_reads(genome_length,denovo_positions):
    """ Generator that creates reads for the whole genome """

    # Create random parent genotypes 
    mom,dad = [random.choice(ALPHABET) for _ in range(2)]
    for base_pos in xrange(genome_length) : 
        yield (mom,dad,create_seqreads(mom,dad,\
                (base_pos in denovo_positions)))

def infer_trio_knownparents(mom,dad,kid):
    """ 
    Base Calling with exact knowledge of parents

    Returns: log probability of denovo event


    """
    uniquebases_child =  set(kid.keys()).difference([mom,dad])
    seqdepth = sum(kid.values())
    if len(uniquebases_child) > 0:
        return 0 #  log prob of denovo is 1
    if mom == dad:
        return np.log(0.5)*seqdepth # sequence depth
    else : 
        pass
        #TODO: Needs to be completed

def infer_trio_unknownparents():
    """ Base Calling with Reads from parents"""
    pass

if __name__ == '__main__' : 

    # Parse commandline  options 
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Commandline options for denovo "+\
            "mutations simulator")
    parser.add_argument("--ncpus",type=int,help="Number of parallel processes",\
            default=None)
    args = parser.parse_args()

    # Get the positions of the denovo mutations
    denovo_positions = sorted(random.sample(xrange(GENOME_LENGTH),30))
    infer_algos = [\
            infer_trio_knownparents,\
            infer_trio_unknownparents,\
            ]

    for base_pos,reads in enumerate(gen_reads(GENOME_LENGTH,\
                                              denovo_positions)) :
        mom,dad,kid_reads = reads
        if base_pos in denovo_positions:
            # ---  BREAKPOINT --- 
            import pdb; pdb.set_trace() 
        if base_pos%1000==0 :
            print("Checking Base Pos: {}".format(base_pos))
        





