from fabric.api import *
import xml.etree.ElementTree as e



hostlist = ("work","lane")

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
def pbsnodes(dtype='xml')	:
	""" Get XML pbsnodes data """
	if dtype == 'xml' : 
		return run("pbsnodes -x")
	else : 
		return run("pbsnodes")

def linesep() :
	print("-"*30)


def getstatus(status,arg='state') :
	""" Returns the status from a status list"""
	if status=="None" :
		return status
	for val in status.split(',') :
		if arg in val : 
			return val.split("=")[1]


def get_free(root) : 
	""" Get free nodes"""
	nodes = root.findall('Node')
	names = [node.find('name').text for node in nodes]
	statuses = []
	for node in nodes : 
		if node.find('status') is not None: statuses.append(node.find('status').text)
		else : statuses.append("None")
	states = [getstatus(status,'state') for status in statuses]
	return zip(names,states)
	
		

if __name__ == '__main__' : 
	linesep()
	m = execute(hostname)
	print("#### Hostnames #####")
	print(m)

	#--------------------------
	# Get XML data
	linesep()
	xmldict = execute(pbsnodes)
	print("### XML output #####")
	for host in hostlist : 
		xmldict[host] = e.fromstring(xmldict[host])
		print("Free hosts in {}".format(host))
		root = xmldict[host]
		for name,state in get_free(root) : 
			print("node={} : state={}".format(name,state))
		
	#-------------------------
	# 	
