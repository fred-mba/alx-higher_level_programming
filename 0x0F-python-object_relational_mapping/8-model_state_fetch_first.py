#!/usr/bin/python3
"""
Module prints the first State object from the database
hbtn_0e_6_usa via sqlalchemy module
"""
from sys import argv
from unittest.runner import _ResultClassType
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State).order_by(State.id).first()

    if results:
        print("{}: {}".format(results.id, results.name))
    else:
        print("Nothing")
    session.close()
