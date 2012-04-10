""" Fetch records one by one. so that you don't eat up all the mem """

import sqlite3 as lite
import sys

with lite.connect("test.db") as con : 	
	cur = con.cursor()
	cur.execute("SELECT * from Cars")
	for row in cur : 
		print row[0],row[1],row[2]

