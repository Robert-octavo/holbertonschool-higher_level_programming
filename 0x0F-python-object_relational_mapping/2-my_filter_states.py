#!/usr/bin/python3
""" Write a script that takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # db = MySQLdb.connect(user=sys.argv[1], db=sys.argv[2])
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'".format(sys.argv[4]))
    # result = cursor.fetchone()
    # print(result)
    [print(state) for state in cursor.fetchall()]
