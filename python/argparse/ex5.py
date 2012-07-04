"""
Inherits arguments from parents
"""

import argparse, sys

if __name__ == '__main__' : 
	parent_parser = argparse.ArgumentParser(add_help=False)
	parent_parser.add_argument("--parent",type=int)

	foo_parser = argparse.ArgumentParser(parents=[parent_parser])
	foo_parser.add_argument("foo")
	print foo_parser.parse_args("--parent 1 hello".split())
	
	bar_parser = argparse.ArgumentParser(parents=[parent_parser])
	bar_parser.add_argument("--bar",action='store_true')
	print bar_parser.parse_args("--bar".split())
