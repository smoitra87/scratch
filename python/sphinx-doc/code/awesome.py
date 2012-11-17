"""
This module is for pure awesomeness

""" 

import os,sys

class Cool(object) : 
	""" This is a really cool class"""
	def dispcool(self,item) : 
		""" Display item Google Cool style
		
		Takes an item. Thinks about the zen beauty in displaying 
		it properly and then displays it to you

		Args:
			item: Any object that has a string representation

		Returns:
			None : It is quite stingy about returning anything.
	
		Raises: 
			Doesn't raise anything

		"""
		print("{0}".format(item))

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

	def dispultracool(self, item,n=20) : 
		"""  Display item, ultracool style 
		
		:param item: Print this item
		:param n: Print this n times
		:type n: integer
		:rtype: None
			
		"""
		print("{0}".format('*'*n+item+'*'*n))


if __name__ == '__main__' : 
	uc = UltraCool("Khan") 	
	uc.disp()
