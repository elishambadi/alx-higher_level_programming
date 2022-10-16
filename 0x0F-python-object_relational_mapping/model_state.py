#!/usr/bin/python3


"""
    State Definition - SQL Alchemy
"""

import sqlalchemy
import MySQLdb
import sys

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+mysqldb://root:##Spidey43##@localhost')
Base = declarative_base()


class State(Base):

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
