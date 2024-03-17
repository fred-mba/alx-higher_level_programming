#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])

    cursor = db.cursor()

    mysqlQuery = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states
        ON cities.state_id = states.id
    ORDER BY cities.id
    """

    cursor.execute(mysqlQuery)

    states_row = cursor.fetchall()

    for state in states_row:
        print(state)
