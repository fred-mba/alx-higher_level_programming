#!/usr/bin/python3
"""
Takes in the name of a state as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


def list_cities_by_state(username, password, database_name, state_name):
    try:
        db = MySQLdb.connect(host='localhost', port=3306,
                             user=username, passwd=password, db=database_name)
        cursor = db.cursor()

        mysqlQuery = "SELECT cities.id, cities.name, states.name FROM cities\
        JOIN states ON cities.state_id = states.id WHERE states.name = %s\
            ORDER BY cities.id ASC"

        cursor.execute(mysqlQuery, (state_name,))

        cities = cursor.fetchall()

        for city in cities:
            print(city)

        cursor.close()
        db.close()

    except MySQLdb.Error as err:
        print(err)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database>\
              <state_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    list_cities_by_state(username, password, database, state_name)
