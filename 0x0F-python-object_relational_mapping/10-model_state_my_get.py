#!/usr/bin/python3
'''
    Task 10
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
    N = sys.argv[4]

    m = "mysql://{}:{}@{}:3306/{}".format(MY_USER, MY_PASS, MY_HOST, MY_DB)
    engine = create_engine(m, encoding='latin1')
    conn = engine.connect()
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
#   N = "%s", (N,)
    session = Session()
#   print(state)
    sess = session.query(State).filter_by(name=N)
    flag = 0
    for state in sess:
        if state.name == N:
            print("{}".format(state.id))
            flag = 1
    if flag == 0:
        print("Not found")
    session.close()
