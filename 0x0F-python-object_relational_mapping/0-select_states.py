#!/usr/bin/python3


"""
    Connects to DB using MySQLdb
"""

import sqlalchemy
import MySQLdb

MY_HOST = 'localhost'
MY_USER = 'root'
MY_PASS = '##Spidey43##'
MY_DB = 'hbtn_0e_0_usa'

db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=MY_DB)
cur = db.cursor()
states = cur.execute("SELECT * FROM states")
print("Selected %s rows" % states)

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

if __name__ == "__main__":
    print("Testing...")
