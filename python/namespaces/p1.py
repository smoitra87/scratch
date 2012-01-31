""" This script experiments with namespaces
This is pretty cool, it shows that you can import a method or class 
with the samename from different modules and you get a different version each time 

 """

from p2 import f

def f1() : 
	from p2 import f
	f()
	from p3 import f
	f()

def f2() : 
	f() # Should print I am p2
	#from p3 import f
	#f()

if __name__ == "__main__" : 
	#f1()
	f2()
