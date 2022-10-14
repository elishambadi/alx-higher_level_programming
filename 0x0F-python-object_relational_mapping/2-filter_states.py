#!/usr/bin/python3


"""
    A script that filters states by user-defined name
"""

import sqlalchemy
import MySQLdb
import sys

if __name__ == "__main__":
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]
    states = sys.argv[4]

    db = MySQLdb.connect(host='localhost',
                         user=MY_USER,
                         passwd=MY_PASS,
                         db=MY_DB)
    cur = db.cursor()
    stmt = "SELECT * FROM states WHERE name LIKE BINARY '%s' ORDER BY id ASC" % states
    states = cur.execute(stmt)

    rows = cur.fetchall()
    for row in rows:
        print("(", end="")
        count = 0
        for col in row:
            if count != 1:
                print("%s, " % col, end="")
            else:
                print("'%s'" % col, end="")
            count = count + 1
        print(")")
