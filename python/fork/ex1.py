#!/usr/bin/python

"""
  run_on_me_or_pid_quit PID cmd arg1 arg2

Runs a command after the process PID has completed, or if this process is
interrupted.

Iain Murray, November 2009, January 2010
"""

# "Daemonize" this job to stop it getting killed by KeyboardInterrupt when
# pressing Ctrl-c in an interactive python session.
import os
import time
print("sid %d, pid %d , ppid %d"%(os.getsid(os.getpid()), os.getpid(),os.getppid()))
print "-"*30
time.sleep(1)
pid_ = os.fork()
print("sid %d, pid %d , ppid %d"%(os.getsid(os.getpid()), os.getpid(),os.getppid()))
if pid_ != 0:
    os._exit(0)
os.setsid()
time.sleep(1)
print("sid %d, pid %d , ppid %d"%(os.getsid(os.getpid()), os.getpid(),os.getppid()))
print "-"*30
pid__ = os.fork()
print("sid %d, pid %d , ppid %d"%(os.getsid(os.getpid()), os.getpid(),os.getppid()))
if pid__ != 0:
    os._exit(0)
time.sleep(1)
print("sid %d, pid %d , ppid %d"%(os.getsid(os.getpid()), os.getpid(),os.getppid()))
import sys, os.path, time, signal

pid = sys.argv[1]
proc_file = '/proc/' + pid

def final():
    os.execv(sys.argv[2], sys.argv[2:])
signal.signal(signal.SIGTERM, final)

try:
    while os.path.exists(proc_file):
        time.sleep(2)
finally:
    final()
