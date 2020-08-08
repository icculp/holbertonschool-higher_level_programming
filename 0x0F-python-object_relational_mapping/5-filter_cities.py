#!/usr/bin/python3
'''
    Task 5
'''
import MySQLdb
import sys


if __name__ == '__main__':
    MY_HOST = "localhost"
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]
    STATE = sys.argv[4]

    conn = MySQLdb.connect(host=MY_HOST, port=3306, user=MY_USER,
                           passwd=MY_PASS, db=MY_DB, charset='utf8')
    cur = conn.cursor()
    cur.execute("SELECT GROUP_CONCAT(cities.name SEPARATOR ', ') \
                FROM cities \
                JOIN states \
                ON cities.state_id=states.id \
                WHERE cities.state_id=states.id \
                AND states.name=%s \
                ORDER BY cities.id ASC", (STATE,))
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[0] is not None:
            print(row[0])
        else:
            print()
    cur.close()
    conn.close()
