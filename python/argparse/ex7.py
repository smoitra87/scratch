"""
Demonstrate use of mutually exclusive statements

"""

import argparse,sys

if __name__ == '__main__' :
	parser = argparse.ArgumentParser()
	group = parser.add_mutually_exclusive_group(required=True)
	group.add_argument("--foo",action='store_true')
	group.add_argument("--bar",action='store_true')

	print parser.parse_args(["--foo"])
	print parser.parse_args(["--bar"])
	
	# The next two statements will cause an error to be generate
	print parser.parse_args(["-foo","--bar"])
	print parser.parse_args([])

