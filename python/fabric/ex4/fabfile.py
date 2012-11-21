" File transfer with sudo. You can transfer to /usr/bin etc."""
from fabric.api import *

env.hosts=['lanec1.compbio.cs.cmu.edu','workhorse.lti.cs.cmu.edu']
env.user='subhodee'

def file_send(localpath,remotepath):
	print("Env Host_str:%s"%env.host_string)
	put(localpath,remotepath)

def file_get(remotepath,localpath) : 
	""" Not give full localhost name """
	get(remotepath,localpath+"."+env.host)


def command(cmd) : 
	""" Run a command on remote """
	run(cmd)

