"""
Argparse program with default args, suppress, store_const = fn + float, 
type checking, nargs, metavar, choices, required, help,dest
"""

import argparse, sys

if __name__ == '__main__' : 
	parser = argparse.ArgumentParser(prog="awesomeness",description=\
	"A lot of options about the argparse module packed into one prog",\
	epilog="Display me after help message",version="0.1.0")

	# The different action statemtns
	parser.add_argument("--foo1",default="obama",action='store')
	parser.add_argument("--foo2",default=0,action='store_const',\
		const=42)
	parser.add_argument("--float",default=int,action='store_const',\
		const=float)
	parser.add_argument("--verbose",action='store_true')
	parser.add_argument("-q","--quiet",action="count")
	parser.add_argument("-i",action="append",help="many integer values")

	# Demonstrate the use of nargs and metavar
	parser.add_argument("--narg1",nargs=2,metavar=("N1","N2"))
	parser.add_argument("--narg2",nargs='+')
	parser.add_argument("--narg3",nargs='?')
	parser.add_argument("--narg4",nargs='*')
	parser.add_argument('args',nargs=argparse.REMAINDER)
	
	# Demonstrate the use of default argparse.SUPPRESS
	parser.add_argument("--bla",default=argparse.SUPPRESS,\
		action='store_const',const=42)

	# Demonstrate the use of type and choices
	parser.add_argument("--type1",type=int)

	def cheese_type(s) : 
		""" Checks for presence of cheese in string """
		if 'cheese' not in s : 
			msg = 'No cheese in %s'%(s)
			raise argparse.ArgumentTypeError(msg)
		return s

	parser.add_argument("--cheese",type=cheese_type,\
		help="Only strings that have cheese")

	parser.add_argument("--singledig",type=int,choices=range(10))

	# Demonstrate the use of required and dest
	parser.add_argument("--run",dest="exec",action='store_true',\
		required=True)

	args = parser.parse_args()
	print(args)
	print("The name of the prog according to sys.argv[0] : %s"%\
		(sys.argv[0]))
	print("The args passed to sys.argv are : %s"%(sys.argv[1:]))



