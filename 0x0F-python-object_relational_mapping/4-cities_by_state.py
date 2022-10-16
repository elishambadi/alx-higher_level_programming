#!/usr/bin/python3


"""
    An SQLi-safe script that filters states by user-defined name
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
    stmt = """
           SELECT cities.id, cities.name, states.name FROM cities
           INNER JOIN states ON states.id = cities.state_id ORDER BY cities.id
           """
    states = cur.execute(stmt)

    rows = cur.fetchall()
    for row in rows:
        print("(", end="")
        count = 0
        for col in row:
            if count == 2:
                print("'%s'" % col, end="")
            else:
                if count == 0:
                    print("%s, " % col, end="")
                else:
                    print("'%s', " % col, end="")
                count = count + 1
        print(")")

    cur.close()
    db.close()
