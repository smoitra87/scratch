import os,sys
from collections import defaultdict
import numpy as np

if __name__ == '__main__' :
    from argparse import ArgumentParser
    parser = ArgumentParser("Reformat calls file")
    parser.add_argument("logfile",type=str)
    parser.add_argument("newfile",type=str)


    args = parser.parse_args()

    skip1 = "denovo candidate at "
    len_skip1 = len(skip1)
    skip2 = "position "
    len_skip2 = len(skip2)

    chromPos = {}
    chromCount =  defaultdict(int)

    with open(args.logfile) as fin, open(args.newfile,'w') as fout:
        for line in fin : 
            line = line[len_skip1:]
            line = line.split(";")[0]
            chrom, pos = line.split(":")
            pos = int(pos[len_skip2:])
            fout.write("{0},{1}\n".format(chrom,pos))









