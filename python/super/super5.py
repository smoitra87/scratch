""" Testing the super function """

import logging
logging.basicConfig(level=logging.INFO)

class LoggingDict(dict) : 
	def __setitem__(self,key,val) : 
		logging.info('Setting %r to %r'%(key,val))
		super(LoggingDict,self).__setitem__(key,val)


ld = LoggingDict([('a',1),('b',2)])
ld['b'] = 2.1
