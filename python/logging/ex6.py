"""
Logger, Handler, Formatter using Python Code
"""

import logging
reload(logging)


class dummy(object) : 
	def __init__(self,_s) : 
		self.s = _s 
	def __str__(self) : 
		return 'dummy:'+self.s

logger = logging.getLogger(__name__) 
logger.setLevel(logging.DEBUG)

kwargs = {'filename':'ex6.log'}
ch = logging.FileHandler(**kwargs)

format_str = "%(asctime)s %(name)s %(levelname)s %(message)s"
formatter = logging.Formatter(format_str)

ch.setFormatter(formatter)
ch.setLevel(logging.DEBUG)

logger.addHandler(ch)

logger.debug(dummy('Hello'))
logger.info(dummy('World'))
logger.warning(dummy('spam'))



