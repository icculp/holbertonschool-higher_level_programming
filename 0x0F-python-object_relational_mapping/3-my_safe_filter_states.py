#!/usr/bin/env python3
'''
    Task 3
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
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                (STATE,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()