from fabric.api import *

env.hosts=["subhodee@linux.gp.cs.cmu.edu","pisa.lti.cs.cmu.edu"]
env.user="subhodeep"

def hostname_check() : 
	run("hostname")

