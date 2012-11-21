from fabric.api import *

env.hosts=["subhodee@linux.gp.cs.cmu.edu","pisa.lti.cs.cmu.edu"]
env.user="subhodeep"

def hostname_check() : 
	""" Check the hostname """
	run("hostname")

def command(cmd) : 
	""" Run any command on remote """
	run(cmd)

@parallel
def pcmd(cmd):
	""" Run commands in parallel """
	run(cmd)

