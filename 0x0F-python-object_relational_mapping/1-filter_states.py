#!/usr/bin/python3
# Write a script that lists all states with a name starting with N (upper N) 
# from the database hbtn_0e_0_usa

import sys
import MySQLdb

db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cursor = db.cursor()
cursor.execute("SELECT * FROM states WHERE name LIKE 'N%'")
[print(state) for state in cursor.fetchall()]
