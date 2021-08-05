#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""


import MySQLdb
import sys


def main():
    """main entry point"""

    connection_data_base = MySQLdb.connect(host="localhost",
                                           port=3306,
                                           user=sys.argv[1],
                                           passwd=sys.argv[2],
                                           db=sys.argv[3])

    cursor = connection_data_base.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

    query_rows = cursor.fetchall()

    for row in query_rows:
        print(row)
    cursor.close()
    connection_data_base.close()


if __name__ == '__main__':
    main()
