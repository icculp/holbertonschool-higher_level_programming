#!/usr/bin/env python3
'''
    Task 8
'''
from model_state import Base, State
from sqlalchemy import create_engine, select, Table, MetaData
import sys


if __name__ == '__main__':
    MY_HOST = "localhost"
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]

    m = "mysql://{}:{}@{}:3306/{}".format(MY_USER, MY_PASS, MY_HOST, MY_DB)
    engine = create_engine(m, encoding='latin1')
    conn = engine.connect()
    meta = MetaData(engine)
    table = Table('states', meta, autoload=True, autoload_with=engine)
    slct = select([table]).where(table.c.id == 1)
    res = conn.execute(slct)
    for row in res:
        print(row)
