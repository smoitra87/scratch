"""
Ex1.py - Basic program that takes a description, a simple flag, 
a double flag, an argument and help statement

$ python ex1.py -f hello --bar 1
"""
import argparse,sys

if __name__ == '__main__'  :
	parser = argparse.ArgumentParser(description="A very simple\
	Argument Parser")
	parser.add_argument("-f","--foo",help="Just a foo statement")	
	parser.add_argument("--bar",help="A bar statement")
	parser.add_argument("baz",nargs='?',help="Just a baz argument")
	args = parser.parse_args()
	print args


