"""
Do error handling and context manager stuff
"""

from fabric.api import *
from contextlib import contextmanager

env.hosts =['pisa.lti.cs.cmu.edu']
env.user='subhodeep'
env.warn_only=False

@contextmanager
def rollbackwrap() : 
	""" Basically places this code block around the function being called"""
	try : 
		yield
	except SystemExit : 
		rollback()
		abort("Fail!")

@contextmanager
def settingwrap() : 
		with settings(warn_only=True) : 
			yield

@task
def multitask() : 
	with rollbackwrap() : 
		task1()
		task2()

def task1() : 
	sudo("apt-get -y install python-numpy")

def task2() : 
	sudo("apt-get -y install python-scipy")

def rollback() :
	sudo("apt-get -y automremove python-numpy")
	sudo("apt-get -y automremove python-scipy")

	
