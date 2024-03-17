#!/usr/bin/python3
"""This module lists all states"""
import MySQLdb
import sys

from requests import session


def list_states(username, password, database):
    """Function to connect to mysql server"""
    db = MySQLdb.connect(
        host="localhost", port=3306, user=username,
        passwd=password, db=database)

    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id")

    states = cursor.fetchall()

    for state in states:
        print(state)

    db.close()


if __name__ == '__main__':
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(username, password, database)
