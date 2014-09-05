import os,sys
from collections import defaultdict
import numpy as np


if __name__ == '__main__' :
    from argparse import ArgumentParser
    parser = ArgumentParser("Read Calls file")
    parser.add_argument("logfile",type=str)

    args = parser.parse_args()

    skip1 = "denovo candidate at "
    len_skip1 = len(skip1)
    skip2 = "position "
    len_skip2 = len(skip2)

    chromPos = {}
    chromCount =  defaultdict(int)

    with open(args.logfile) as fin :
        for line in fin : 
            line = line[len_skip1:]
            line = line.split(";")[0]
            chrom, pos = line.split(":")
            pos = int(pos[len_skip2:])
            chromPos[chrom] = pos
            chromCount[chrom] += 1

    chromCount = dict(chromCount)

    posFreq = np.asarray([chromPos[chrom]/float(chromCount[chrom]) for chrom in chromPos])

    for idx, chrom in enumerate(chromPos) : 
        print("{} : 1 in {} bp".format(chrom,posFreq[idx]))

    print
    print("Mean BasePair Freq : {}".format(posFreq.mean()))
    print("Std BasePair Freq : {}".format(posFreq.std()))


    import matplotlib.pyplot as plt
    fig,ax = plt.subplots()

    ax.plot(posFreq,"-*")
    ax.set_title("Frequency of occurence of denovo base pairs")
    ax.set_xlabel("Contigs")
    ax.set_ylabel("Frequency occurence")
    fig.set_size_inches(12,10)


    ax.set_xticks(range(len(chromPos)))
    ax.set_xticklabels(chromPos.keys())
    ax.set_xlim([-1,len(chromPos)+1])

    plt.show()










