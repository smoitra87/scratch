""" I am a test module"""

from nose.tools import *

import ex6

def test_f1() : 
	""" I am a test case """
	eq_(ex6.subex6.spam.eggs(),1)
	
