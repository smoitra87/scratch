"""
Tests loading module and executes accordingly

"""

class A : 
	def __init__(self,*args,**kwdargs) : 
		if __name__ == '__main__' : 
			assert args[0] == 'helloworld'
		else : 
			assert args[0] == 1
			assert kwdargs['bla'] == "really bla"
		print "__name__ is ", __name__


if __name__ == '__main__' : 
	a = A('helloworld')


