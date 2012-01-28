#! /usr/bin/env python
""" 
This program has some examples for basic python logging

"""

import sys
import logging
reload(logging) # This statement is just there cuz ipython does not
# reload the same module many times


logging.basicConfig(filename="bar.log",filemode="w",
level=logging.DEBUG)
logging.info("hello")
logging.debug("world")
logging.error("bla")

