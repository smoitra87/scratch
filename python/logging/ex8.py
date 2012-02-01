""" Tests if Loggers defined in one class can be used elsewhere """

import logging

class LoggerEx8(object) : 
	""" Tests whether loggers can be used from class objects"""
	#def __init__(self) :
	""" Initializer for Logger class""" 
	handler_p = {
		'filename' : 'ex8.log',
		'mode' : 'a'
	}
	fh = logging.FileHandler(**handler_p)
	fh.setLevel(logging.INFO)
	
	
	ch = logging.StreamHandler()
	ch.setLevel(logging.WARNING)
		

	fmtstr = '%(name)s %(levelname)s %(message)s' 
	fm = logging.Formatter(fmtstr)
	ch.setFormatter(fm)
	fh.setFormatter(fm)

	logger = logging.getLogger('base')
	logger.setLevel(logging.DEBUG)
	logger.addHandler(fh)
	logger.addHandler(ch)
	
	ch2 = logging.StreamHandler()
	ch2.setLevel(logging.WARNING)
	fmtstr = 'ch2: %(name)s %(levelname)s %(message)s' 
	fm = logging.Formatter(fmtstr)
	ch2.setFormatter(fm)
	
	logger2 = logging.getLogger('base.foo')
	logger2.setLevel(logging.DEBUG)
	#logger2.addHandler(fh)
	logger2.addHandler(ch2)
	
def foo() : 
	logger = LoggerEx8.logger
	logger.warning('Warning from foo')


if __name__ == '__main__' :
	""" Main call for Testing purposes""" 
	logger = LoggerEx8.logger
	logger.debug('Debug Message')	
	logger.info('Info Message')
	logger.warning('Warning message')
	logger.warning('Warning message2')

	
	logger2 = LoggerEx8.logger2
	logger2.debug('Debug Message')	
	logger2.info('Info Message')
	logger2.warning('Warning message')
	logger2.warning('Warning message2')

	foo()


