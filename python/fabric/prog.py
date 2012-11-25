""" 
using fabric as a library without having to call the 
"""

from fabric.api import run,execute,hosts



@hosts('subhodeep@pisa.lti.cs.cmu.edu:22')
def return_user() : 
	""" Runs whoami on remote host """
	run('whoami')

if __name__ == '__main__' :
	execute(return_user)
	
	# Can also execute arbitrary commands and save the output
	out = execute(hosts('subhodeep@pisa.lti.cs.cmu.edu')(lambda : run('uname -a')))
	print(out)
