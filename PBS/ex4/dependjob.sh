#!/bin/sh


jobid=$(qsub -v VAL=1 depend.qsub | cut -d. -f1)
jobid=$(qsub -v VAL=2 -W depend=afterok:$jobid depend.qsub | cut -d. -f1 )
qsub -v VAL=3 -W depend=afterok:$jobid depend.qsub
