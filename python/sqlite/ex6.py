""" This performs autoincrement of the primary key and can hence be 
used to retreive the alst rowid """

import sqlite3 as lite
import sys

with lite.connect("test.db") as con : 
	cur = con.cursor() 
	cur.execute("CREATE TABLE Friends(Id INTEGER PRIMARY KEY, Name\
			TEXT)")
	cur.execute("INSERT INTO Friends(Name) VALUES ('Tom');")
	cur.execute("INSERT INTO Friends(Name) VALUES ('Rebecca');")
	cur.execute("INSERT INTO Friends(Name) VALUES ('Jim');")
	cur.execute("INSERT INTO Friends(Name) VALUES ('Robert');")

	lid = cur.lastrowid
	print "Last Row id is %d"%lid

