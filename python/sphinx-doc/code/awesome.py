"""
This module is for pure awesomeness

.. moduleauthor:: Subhodeep Moitra<smoitra@cs.cmu.edu>

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

		.. note::
			We are not going to talk about other coool classes
		
		Intersphinx can be used to refer other cool modules such as 
		:mod:`os`, :mod:`sys` and :mod:`itertools`. 

		Can intersphinx get ``Bio.Align.Generic.Alignment`` ? 
		:class:`Bio.Align.Generic.Alignment` ? I guess not.  


		There are a 


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

def foo(n) : 
	""" The original foo function 
	
	Let's say you want to use this function. You may do so like::
		>>> print(foo(10))
		55

	Be **careful** when using :func:`foo` since it is a child
	of :class:`Cool` and it might get jealous. But they are all members
	of :mod:`awesome`

	"""
	return (n*(n+1))/2


if __name__ == '__main__' : 
	uc = UltraCool("Khan") 	
	uc.disp()
