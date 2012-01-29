""" Performs logging using config files"""

import logging
import logging.config

# Load the config file
logging.config.fileConfig('ex4.conf')

# Load the logger from file
logger = logging.getLogger('myLogger')

# Start logging
logger.debug('msg1')
logger.info('msg2')
logger.warning('msg3')

