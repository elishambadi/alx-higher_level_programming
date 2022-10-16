#!/usr/bin/python3


"""
    An SQLi-safe script that filters cities by user-defined name
"""

import sqlalchemy
import MySQLdb
import sys

if __name__ == "__main__":
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]
    state_input = sys.argv[4]
    invalid = ';'
    if invalid in state_input:
        print("Invalid input")
        exit(0)

    db = MySQLdb.connect(host='localhost',
                         user=MY_USER,
                         passwd=MY_PASS,
                         db=MY_DB)
    cur = db.cursor()
    stmt = """
           SELECT cities.name
           FROM cities
           INNER JOIN states
           ON states.id = cities.state_id
           WHERE states.name = '{state}'
           ORDER BY cities.id
           """.format(state=state_input)
    states = cur.execute(stmt)

    rows = cur.fetchall()
    count = 0
    for row in rows:
        for col in row:
            if count == 0:
                print("%s" % col, end="")
            else:
                print(", %s" % col, end="")
            count = count + 1
    print("")

    cur.close()
    db.close()
