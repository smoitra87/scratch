from fabric.api import *
import xml.etree.ElementTree as e



hostlist = ("work",)

def decorateall(func) :
	@hosts(*hostlist)
	@with_settings(use_ssh_config=True,capture=True)
	def decoratedfunc(*args,**kwdargs) : 
		return func(*args,**kwdargs)
	return decoratedfunc

@decorateall
def hostname() : 
	""" Check the hostname """
	return run("hostname")

@decorateall
def hadoopjobstatus_workhorse() :
	""" Get the hadoop job status """
	return run("ssh leo ssh pdl hadoop job -list")

@hosts("pdl")
@with_settings(use_ssh_config=True,capture=True)
def hadoopstatus() : 
	return run("hadoop job -list")



def linesep() :
	print("-"*30)


	

if __name__ == '__main__' : 
	linesep()
	m = execute(hostname)
	print("#### Hostnames #####")
	print(m)

	
	#-------------------------
	# Get hadoop status
	linesep()
	print("#### HADOOP from Workhorse####")
	print(execute(hadoopjobstatus_workhorse))

	linesep()
	print("### HADOOP from Leo ####")
	print(execute(hadoopstatus))
