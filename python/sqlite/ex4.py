""" Execute many statements at once using a tuple of tuples"""

import sqlite3 as lite
con = lite.connect("test.db")

cmd = (
	(1,'Audi',10000),
	(2,'Ferrari',20000),
	(2,'Ford',4000)
)

with con : 
	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS Cars")
	cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
	cur.executemany("INSERT INTO Cars VALUES(?,?,?)",cmd)
