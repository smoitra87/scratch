""" File transfer with sudo. You can transfer to /usr/bin etc."""
from fabric.api import *

env.hosts=['pisa.lti.cs.cmu.edu']
env.user='subhodeep'

def file_send(localpath,remotepath):
	print("Env Host_str:%s"%env.host_string)
	put(localpath,remotepath,use_sudo=True)

def command(cmd) : 
	""" Run a command on remote """
	run(cmd)

