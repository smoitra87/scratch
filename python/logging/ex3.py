"""
Logger, Handler, Formatter using Python Code
"""

import logging
reload(logging)

logger = logging.getLogger(__name__) 
logger.setLevel(logging.DEBUG)

kwargs = {'filename':'ex3.log'}
ch = logging.FileHandler(**kwargs)

format_str = "%(asctime)s %(name)s %(levelname)s %(message)s"
formatter = logging.Formatter(format_str)

ch.setFormatter(formatter)
ch.setLevel(logging.DEBUG)

logger.addHandler(ch)

logger.debug('Hello')
logger.info('World')
logger.warning('spam')
