""" 
Explorin python string formatting opytions 

These are old style string formatting options much like sprintf. These
are different from .format options that py3k has adopted

"""

# Showing that %s accepts any object with an __str__ method

class A(object) : 
	""" A dummy string class"""
	def __init__(self,_s) : 
		self.s = _s
	def __str__(self) :
		""" Defining custom function for str """
		return self.s + "kapow!"

a = A('boom!')
print("The string is %(object_a)s"%({'object_a':a}))

######################################################################
# String formatting options

# Specifying args alone
print "%s : %s" %('foo','bar')

# specifying named args
print "%(a)s : %(b)s" %{'a':'foo','b':'bar'}

# Specifying mixture of args and named args is not allowed


# workign with floats 
x = 10000/3.0
print "Default print x : ", x

# print exponential form
print "exponential : %e" % x

# constrict to max 2 dec places
print "2 dec only x : %.2f"% x

# Expnd to 15 dec places
print "15 dec places x : %.15f" % x

# 15 dec and 6 length padded with zeros
print "2 dec and 8 zero padded fields x : %08.2f"%x


