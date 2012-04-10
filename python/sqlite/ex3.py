""" Create a Table and insert values into it"""

import sqlite3 as lite

con = lite.connect("test.db")

with con :
	cur = con.cursor()
	cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
	cur.execute("INSERT INTO Cars VALUES(1,'Audi',10000)")
	cur.execute("INSERT INTO Cars VALUES(2,'Ford',20000)")
	cur.execute("INSERT INTO Cars VALUES(3,'Ferrari',40000)")
