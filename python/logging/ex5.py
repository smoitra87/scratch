""" Performs logging using config files"""

import logging
import logging.config

# Load the config file
logging.config.fileConfig('ex4.conf')

# Load the logger from file
logger1 = logging.getLogger('foo')
logger = logging.getLogger('foo.bar')

# Start logging
logger.debug('msg1')
logger.info('msg2')
logger.warning('msg3')

