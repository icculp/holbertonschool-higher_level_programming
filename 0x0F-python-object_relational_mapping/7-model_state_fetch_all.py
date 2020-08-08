#!/usr/bin/python3
'''
    Task 7
'''
from model_state import Base, State
from sqlalchemy import create_engine, select, Table, MetaData
import sys
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    MY_HOST = "localhost"
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]

    m = "mysql://{}:{}@{}:3306/{}".format(MY_USER, MY_PASS, MY_HOST, MY_DB)
    engine = create_engine(m, encoding='latin1')
    conn = engine.connect()
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
'''
    m = "mysql://{}:{}@{}:3306/{}".format(MY_USER, MY_PASS, MY_HOST, MY_DB)
    engine = create_engine(m, encoding='latin1')
    conn = engine.connect()
    meta = MetaData(engine)
    table = Table('states', meta, autoload=True, autoload_with=engine)
    slct = select([table])
    res = conn.execute(slct)
    for row in res:
        print(row)
'''
