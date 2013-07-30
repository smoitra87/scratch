from fabric.api import *

env.use_ssh_config= True
env.hosts=["work","lang"]

def hostname() : 
	""" Check the hostname """
	run("hostname")

if __name__ == '__main__' : 
	hostname()
