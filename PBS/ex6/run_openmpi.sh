#!/bin/sh
#PBS -lnodes=2:ppn=2,walltime=1000

# list the name of the nodes participating in the job. pbsdsh can run
# any command in parallel
pbsdsh uname -n

. /opt/torque/etc/openmpi-setup.sh

cd $PBS_O_WORKDIR
mpirun mpi-verify.openmpi.x

date

