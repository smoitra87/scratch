"""
decorators that change something about the function
"""

def give_respect(func) : 
	func.respect = True
	return func

@give_respect
def f() : 
	""" I do nothing"""
	print("Hello World")

def give_hate(curse) : 
	def give_respect(func) : 
		func.respect = curse
		return func
	return give_respect

@give_hate('dumbwit')
def g() : 
	""" I do nothing """
	print("Hello World")

def exec_f(f) :
	f()
	print("Name of func is",f.func_name)
	print('func doc',f.__doc__)
	print(f.respect)

if __name__ == '__main__' : 
	exec_f(f)
	exec_f(g)
	exec_f(f)
