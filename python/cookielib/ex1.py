"""
This program demonstrates the use of cookielib and what to do when
a module is not available

Code is at : 
http://code.activestate.com/recipes/302930-cookielib-example/

"""

cookielib=None
ClientCookie=None
cj=None

COOKIEFILE = "cookie.lwp"

import os

try : 
	import cookielib
except ImportError : 
	pass
else :
	import urllib2
	urlopen = urllib2.urlopen
	cj = cookielib.LWPCookieJar()
	Request = urllib2.Request

if not cookielib : 
	try :
		import ClientCookie 
	except ImportError : 
		import urllib2
		urlopen = urllib2.urlopen
		Request = urllib2.urlopen
	else : 
		urlopen = ClientCookie.urlopen
		cj = ClientCookie.LWPCookieJar()
		Request = ClientCookie.Request

if cj is not None : 
	if os.path.isfile(COOKIEFILE) :
		cj.load(COOKIEFILE)
	if cookielib : 
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj)) 
		urllib2.install_opener(opener)
	else : 
		opener = ClientCookie.build_opener(\
			ClientCookie.HTTPCookieProcessor(cj))
		ClientCookie.install_opener(opener)
		

theurl = 'http://www.google.com'
txdata = None
txheaders = {'User-agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:13.0) Gecko/20100101 Firefox/13.0.1'} 

try :
	req = Request(theurl,txdata,txheaders)
	handle = urlopen(req)
except IOError, e : 
	print("Could not open %s"%(theurl))
	if hasattr(e,'code') : 
		print("The error code is %s"%(e.code))
else : 
	print("The headers of the page are ")
	print handle.info()

print # Use of single print statement to generate a blank line

if not cj : 
	print "No cookie available for you"
else : 
	print("These are the cookies we have received so far")
	for i,cookie in enumerate(cj) :
		print i, " : ", cookie
	cj.save(COOKIEFILE)
