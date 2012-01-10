""" Set up script """

from distutils.core import setup, Extension

setup(
	name  = "ex7",
	version = '0.1.0',
	url = 'http://gitub.com/smoitra87',
	author = 'Subhodeep Moitra',
	author_email = 'subho@cmu.edu',
	license = 'BSD License',
	packages = ['ex7','tests'],
	ext_modules = [Extension('ex7.foo',sources=['ex7/foo.c'])]
	)
