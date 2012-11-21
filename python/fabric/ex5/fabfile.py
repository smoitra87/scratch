""" Create a fabfile that uses context managers and conditional 
execution based on success of a job """


from fabric.api import *
#env.hosts=['workhorse.lti.cs.cmu.edu','lanec1.compbio.cs.cmu.edu']
#env.user="subhodee"

env.hosts=['subhodeep@pisa.lti.cs.cmu.edu']

env.skip_bad_hosts=True
env.timeout=2
env.parallel=True # This makes all the functions parallel by default

def file_send_mod(localpath,remotepath,mod) :
	""" Send a file such that is has the following mode """
	put(localpath,remotepath,mode=int(mod,8))

@serial # Force a function to be run in series
def cmd(cmd) :
	""" Run a command in sudo if it fails""" 
	with settings(warn_only=True) : 
		if run(cmd).failed :
			sudo(cmd)




