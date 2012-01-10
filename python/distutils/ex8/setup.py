""" Set up script """

from distutils.core import setup, Extension

setup(
	name  = "ex8",
	version = '0.1.0',
	url = 'http://gitub.com/smoitra87',
	author = 'Subhodeep Moitra',
	author_email = 'subho@cmu.edu',
	license = 'BSD License',
	packages = ['ex8','tests'],
	package_data = {'ex8':['data/*.dat','*.c']},
	ext_modules = [Extension('ex8.foo',sources=['ex8/foo.c'])],
	scripts = ['runner']
	)
