#!/usr/bin/python3
"""Write a script that lists all cities from the database hbtn_0e_4_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    # db = MySQLdb.connect(user=sys.argv[1], db=sys.argv[2])
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name\
                    FROM states RIGHT JOIN cities\
                    ON states.id = cities.state_id")

    [print(state) for state in cursor.fetchall()]
