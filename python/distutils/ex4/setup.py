""" I am the setup script 
An interesting fact : 
	package_dir has no effect on where the C source files are foind. 
	These need to be specified manually. See below. 

"""

from distutils.core import setup, Extension

setup(
	name='ex3',
	version='0.1.0',
	url='http://github.com/smoitra87',
	author='Subhodeep Moitra',
	author_email='subho@cmu.edu',
	license='BSF license',
	#package_dir={'':'notroot'},
	#packages=[''],
	ext_modules = [Extension('foo',sources=['notroot/foo.c'])]
	);
