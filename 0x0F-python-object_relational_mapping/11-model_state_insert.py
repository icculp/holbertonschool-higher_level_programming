#!/usr/bin/python3
'''
    Task 11
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
    session.add(State(name='Louisiana'))
    session.commit()
    sess = session.query(State).filter_by(name='Louisiana')
    for state in sess:
        print("{}".format(state.id))
    session.close()
