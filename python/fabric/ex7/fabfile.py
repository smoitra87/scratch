"""
Using context managers and task decorators
"""

from fabric.api import * 
env.hosts=["subhodeep@127.0.0.1"]


@task
def cmd(cmd) : 
	run(cmd)
	run('echo '+hello())

@task
def test() : 
	""" Use context managers """
	with settings(user="subhodeep",host_string="pisa.lti.cs.cmu.edu") : 
		run("whoami")
		with cd('/usr/bin') : 
			sudo('touch a.txt ; rm a.txt')

def hello() :
	""" I am used internally """
	return "HEllo World"


