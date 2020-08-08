#!/usr/bin/python3
'''
    Task 14
'''
from model_state import Base, State
from model_city import City
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

    sess = session.query(State, City).filter(City.state_id == State.id)
    for state in sess:
        print("{}: ({}) {}".format(state[0].name, state[1].id, state[1].name))
    session.close()
