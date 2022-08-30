#!/usr/bin/python3
"""Wait, do you remember the previous task? Did you test "Arizona';
TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '" as an input?
"""

import sys
from unittest import result
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name =%s", (sys.argv[4],))
    # result = cursor.fetchone()
    # print(result)
    [print(state) for state in cursor.fetchall()]
# cursor.execute("SELECT * FROM states")
# [print(state) for state in cursor.fetchall() if state[1] == sys.argv[3]]
