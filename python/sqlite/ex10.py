""" Working with SQL Metadata """

import sqlite3 as lite
import sys

with lite.connect("test.db") as con : 

	# Get Table info using the PRAGMA statement
	cur = con.cursor()
	cur.execute("PRAGMA table_info(Cars)")
	
	data = cur.fetchall()
	for d  in data : 
		print d[0],d[1],d[2]


	# Use cur.description metadata

	cur.execute("SELECT * From Cars")
	col_names = [c[0] for c in cur.description]
	rows = cur.fetchall()
	
	print "%s %-10s %s" % (col_names[0], col_names[1], col_names[2])

	for row in rows:    
		print "%2s %-10s %s" % row

		
	# Use the sqlite_master special table

	cur.execute("SELECT Name FROM sqlite_master WHERE TYPE='table'")
	rows = cur.fetchall()
	for row in rows : 
		print row
	

