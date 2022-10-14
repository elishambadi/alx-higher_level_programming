#!/usr/bin/python3


"""
    Connects to DB using MySQLdb
"""

import sqlalchemy
import MySQLdb
import sys

if __name__ == "__main__":
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]

    db = MySQLdb.connect(host='localhost',
                         user=MY_USER,
                         passwd=MY_PASS,
                         db=MY_DB)
    cur = db.cursor()
    states = cur.execute("SELECT * FROM states ORDER BY states.id ASC")

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
