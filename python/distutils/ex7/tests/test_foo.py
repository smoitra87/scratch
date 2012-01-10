""" I am a test module"""

from nose.tools import *

import ex7

def test_f1() : 
	""" I am a test case """
	pass	

def test_ex() :
	""" I test the ext case """
	eq_(ex7.foo.hello(),1)
