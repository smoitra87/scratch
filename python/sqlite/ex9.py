""" Working with parametrized queries 
	For Select commands the rowcount is 0, since no rows get updated
"""

import sqlite3 as lite
import sys

p=10400
Id=1


with lite.connect("test.db") as con  :
	
	cur = con.cursor()
	
	cur.execute("UPDATE Cars SET Price=? WHERE Id=?",(p,Id))
	con.commit()
	print "Number of rows updated %d"%(cur.rowcount)

	

