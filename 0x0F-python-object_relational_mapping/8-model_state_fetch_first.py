#!/usr/bin/python3


"""
    Find cities using SQL Alchemy
"""

import sqlalchemy
import MySQLdb
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    from model_state import Base, State
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    # All classes tied to sqlalchemy imported now. Let's use them!

    Session = sessionmaker(bind=engine)
    session = Session()
    count = 0
    for state in session.query(State).order_by(State.id):
        if count == 0:
            print("{}: {}".format(state.id, state.name))
        else:
            exit(0)
        count = count + 1
