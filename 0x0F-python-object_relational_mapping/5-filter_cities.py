#!/usr/bin/python3
"""
Takes in the name of a state as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])

    cursor = db.cursor()

    mysqlquery = """
    SELECT cities.name
    FROM cities
    JOIN states
        ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id
    """

    cursor.execute(mysqlquery, (argv[4],))

    row_cities = cursor.fetchall()

    cities = ', '.join(city[0] for city in row_cities)
    print(cities)
