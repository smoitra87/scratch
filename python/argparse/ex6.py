"""
Demonstrates the use of subcommands

What's the purpose of subcommands. To give it a git like feature, wherein there are a different set of options for git config and git log

$ python ex6.py --dance log -n 2

"""

import argparse, sys

if __name__ == '__main__' : 
	parser = argparse.ArgumentParser(prog="git")
	parser.add_argument("--dance",action='store_true',help=\
		"make git dance")
	subparsers = parser.add_subparsers(help="Subparser help")

	# Add the status subparser
	parser_status = subparsers.add_parser("status",\
		help="help for status subcommand")
	parser_status.add_argument("-s",'--short',action='store_true',\
		help="Give output in short-format")


	# Add the log subparser
	parser_log = subparsers.add_parser("log",\
		help="help for log subcommand")
	parser_log.add_argument("-n",type=int,help="show prev n logs")

	
	print parser.parse_args()
	
	#	print parser.parse_args("--help".split())
