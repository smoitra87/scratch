""" File transfer and error handling on remote """
from fabric.api import *

env.hosts=['lanec1.compbio.cs.cmu.edu','workhorse.lti.cs.cmu.edu']
env.user='subhodee'

def file_send(localpath,remotepath):
	print("Env Host_str:%s"%env.host_string)
	put(localpath,remotepath)

def command(cmd) : 
	""" Run a command on remote """
	run(cmd)

