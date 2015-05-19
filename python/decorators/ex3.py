""" Illustrates the use of decorator decorator""" 

def mydecorator(func,*args):
    """ My decorator"""
    def wrapper(args):
        """ Wrapper decorator"""
        func(args)
        print "Original function is wrapped"
    return wrapper

@mydecorator
def mysum(l):
    """ Sums stuff up"""
    print reduce(lambda x,y:x+y,l)
print
print "Nested Wrappers"
mysum(range(5))
print mysum.__name__
print mysum.__doc__

from decorator import decorator
@decorator
def mydecorator(func,*args):
    func(args)
    print("Original function is wrapped")

@mydecorator
def mysum(l):
    """ Sums stuff up"""
    print reduce(lambda x,y:x+y,l)
print
print "Decorator Decorator"
mysum(range(5))
print mysum.__name__
print mysum.__doc__


