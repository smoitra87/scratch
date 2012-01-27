""" This program demonstrates the use of some keyword argument passing
 options
"""

# pass an argument and a list

def f1(arg1,*args) : 
	print 'arg1 is ',arg1
	print 'Other args are :'
	for arg in args :
		print arg

# pass an argument and a dict
def f2(arg1,**args) : 
	print 'First arg is ', arg1
	for key in args.keys() :
		print key,args[key]

# pass an argument, list and dict

def f3(arg,*args,**kwargs) : 
	print 'First arg is', arg
	print 'Other args are'
	for arg in args : print arg
	
	print 'The keyword args are '
	for key in kwargs.keys() : 
		print key,kwargs[key]


# pass kwarg eating up part of input 

def f4(a=None,**kwargs) : 
	print 'Extracted a=%r', a
	print 'Remaining args are :' 
	print kwargs


if __name__ == '__main__' : 
	f1(1,'a',1.0)
	print '-------------------------------------------'
	f2(1,a=1,b='a')
	print '-------------------------------------------'
	f3(1,'a',1.0,a=2,b='b',c=1.3)
	print '-------------------------------------------'

	# Unpack a tuple
	args = ['a',1]
	kwargs = {'a':2,'b':'b','c':1.3}
	f3(1,*args,**kwargs)
	print '-------------------------------------------'
	f4(x=1,y='a',a=3)

