"""
A decorator which returns a different and not a decorator
"""

def memoize(func) : 
	""" Apply the memoize pattern """
	def check_square(*args) :
		""" Finds the square """
		if not hasattr(func,'results') : 
			func.results = {}
		if args not in func.results : 
			func.results[args] = func(*args)
			print('Not From Cache')
		return func.results[args]
	return check_square

@memoize
def square(val): 
	""" Squares val """
	return val*val;


if __name__ == '__main__' : 
	print(square(4))
	print(square(4))
	print(square)	
	print(square.__name__)
	print(square.__doc__)

