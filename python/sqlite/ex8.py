""" Work with the dictionary cursor""" 

import sqlite3 as lite
import sys

with lite.connect("test.db") as con : 
	con.row_factory = lite.Row
	cur = con.cursor()
	
	cur.execute("SELECT * From Cars")
	
	rows = cur.fetchall()
	
	for row in rows : 
		print "%s %s %s" % (row['Id'],row['Name'],row['Price'])

