""" This script does logging across different modules"""

import logging
reload(logging) # for ipython to work
import ex2lib
reload(ex2lib)

logging.basicConfig(filename='ex2.log',filemode='w',
level=logging.DEBUG)
logging.info('Started')
ex2lib.f()
logging.info('Ended')



