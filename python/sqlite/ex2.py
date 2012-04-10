""" This program connects to a sqlite db using the withg statement """

import sqlite3 as lite

con = lite.connect("test.db")

with con : 
	cur  = con.cursor()
	cur.execute('SELECT SQLITE_VERSION()')
	data = cur.fetchone()
	print "SQLITE version is ", data


