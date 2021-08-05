#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""


import MySQLdb
import sys


def main():

    connection_data_base = MySQLdb.connect(host="localhost",
                                           port=3306,
                                           user=sys.argv[1],
                                           passwd=sys.argv[2],
                                           db=sys.argv[3])

    cursor = connection_data_base.cursor()

    cursor.execute("SELECT cities.name\
        FROM cities INNER JOIN states ON states.id = cities.state_id\
            WHERE states.name = %s ORDER BY cities.id ASC", (sys.argv[4],))

    query_rows = cursor.fetchall()

    new_list = []

    for row in query_rows:
        for column in row:
            new_list.append(column)

    print(", ".join(new_list))

    cursor.close()
    connection_data_base.close()


if __name__ == '__main__':
    main()
