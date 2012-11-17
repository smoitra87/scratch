"""
This module is for pure awesomeness

""" 

import os,sys

class Cool(object) : 
	""" This is a really cool class"""
	pass	


class _NotCool(object) : 
	""" This is not such a cool class hence I want to keep it private
	"""
	pass
	

class UltraCool(Cool) : 
	""" An UltraCool class which is a tupe of Cool class

	"""
	def __init__(self,name) : 
		""" An initializer For the ultracool class"""
		self.name = name

	def disp(self) :
		""" Print Details about the UltraCool class """
		print("Say my name- {0}".format(self.name))
	




if __name__ == '__main__' : 
	uc = UltraCool("Khan") 	
	uc.disp()
