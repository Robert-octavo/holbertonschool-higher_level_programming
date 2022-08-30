#!/usr/bin/python3
# Write a script that lists all states from the database hbtn_0e_0_usa

import sys
import MySQLdb

# TODO: Create a connection getting the param from the terminal and with cursor
# allow me to execute a query, fetchall() allow me to get all the data. 
# fetchmany(), fetchone()

db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cursor = db.cursor()
cursor.execute("SELECT * FROM `states`")
[print(state) for state in cursor.fetchall()]
