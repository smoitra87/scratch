""" Builds the C extensions needed to parse """

from distutils.core import setup, Extension

setup(
	name = 'File parser',
	version = '0.1.0',
	url = 'http://github.com/smoitra87/scratch/ex9',
	ext_modules=[Extension("cparser",sources=['parser.c'])],
	description='Builds Python Lists and Dicts by reading a file'
	)	
