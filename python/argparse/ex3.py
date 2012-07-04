"""
Disable help with add_help=False
"""

import argparse,sys

if __name__ == '__main__' : 
	parser = argparse.ArgumentParser(add_help=False)
	parser.add_argument("-h","--help",action="store_true")
	args = parser.parse_args()
	print args
	if args.help : 
		print("Yo this is all the help you're gonna get..!")

