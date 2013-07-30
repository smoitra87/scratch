from fabric.api import *
env.use_ssh_config=True
env.hosts=["work","lang"]
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

