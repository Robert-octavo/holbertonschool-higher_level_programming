#!/usr/bin/python3
"""Write a script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    # db = MySQLdb.connect(user=sys.argv[1], db=sys.argv[2])
    cursor = db.cursor()
    cursor.execute("SELECT cities.name\
                    FROM cities INNER JOIN states\
                    ON states.id = cities.state_id\
                    WHERE states.name = %s", (sys.argv[4],))
    # print(", ".join([res[2] for res in cursor.fetchall() if res[4] == sys.argv[3]]))
    print(", ".join([result[0] for result in cursor.fetchall()]))
