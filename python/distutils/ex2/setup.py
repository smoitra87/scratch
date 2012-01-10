""" Set up script """

from distutils.core import setup, Extension

setup(
	name  = "ex2",
	version = '0.1.0',
	url = 'http://gitub.com/smoitra87',
	package_dir = {'':'notroot'},
	py_modules = ['foo','bar']
	)
