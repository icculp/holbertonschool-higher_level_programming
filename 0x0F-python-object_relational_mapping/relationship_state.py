#!/usr/bin/python3
'''
    Task 6
'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    ''' State sqlachlemy '''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete', backref='state')
    '''i don't get the backref, why state not State or states'''
