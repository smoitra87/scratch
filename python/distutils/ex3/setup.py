""" I am the setup script """

from distutils.core import setup, Extension

setup(
	name='ex3',
	version='0.1.0',
	url='http://github.com/smoitra87',
	author='Subhodeep Moitra',
	author_email='subho@cmu.edu',
	license='BSF license',
	ext_modules = [Extension('foo',sources=['foo.c'])]
	);
