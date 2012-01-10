""" I am a test module"""

from nose.tools import *

import ex8

def test_f1() : 
	""" I am a test case """
	pass	

def test_ex() :
	""" I test the ext case """
	eq_(ex8.foo.hello(),1)
