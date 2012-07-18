"""
Exploring string.format

"""

# Using positional args
print "{0} {1} {2}".format(*'abc')
print "{} {} {}".format(*range(3))
print " {2} {1} {0} ".format(*['foo','bar','baz'])
print " {0} {1} {0} ".format('foo','bar')

# Using named args
print "{name} is {age} years old".format(name='foo',age=12)
d = {'name':'foo','age':12}

print "{name} is {age} years old".format(**d)

# Using lists and attributes of objects
print("Real:{0.real} Imag:{0.imag}".format(1+4j))
print("2nd elem of range(1,5) : {l[1]}".format(l=range(1,5)))

# a class that uses the format method to print itself
class Point(object) : 
	""" Uses format to print itself"""
	def __init__(self,x,y) : 
		""" Init the class """
		self.x = x
		self.y = y
	def __str__(self) : 
		""" Print the contents of the class"""
		return "X coord:{self.x} Y coord:{self.y}".format(self=self)

print Point(1,2)

# Using repr and s
print("Using repr:{0!r} ; Using str:{0!s}".format('a\tb'))

# using align params
print '{:*^30}'.format("centered")

# For floats
print '{{val:03.2f}} {val:03.2f}'.format(val=10/3.0)

# Nested evaluations
for align,text in zip('<^>',('left','center','right')) : 
	print("{0:{fill}{align}{width}}".format\
		(text,fill=align,align=align,width=20))





