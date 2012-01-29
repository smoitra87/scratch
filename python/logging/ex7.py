""" Performs logging using config files"""

import logging
import logging.config
import os

# Load the config file
if os.path.exists('ex7.conf') :
	logging.config.fileConfig('ex7.conf')
	# Load the logger from file
	logger = logging.getLogger('myLogger')
else : 
	logger = logging.getLogger()
	logger.addHandler(logging.NullHandler())

# Start logging
logger.debug('msg1')
logger.info('msg2')
logger.warning('msg3')

