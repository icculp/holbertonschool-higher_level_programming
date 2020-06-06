#!/usr/bin/python3
""" 1-main """
from models.rectangle import Rectangle
from models.base import Base
'''
if __name__ == "__main__":

    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)
'''

if __name__ == "__main__":
    b1 = Base()
    print(b1.id)
    b2 = Base()
    print(b2.id)
    b3 = Base()
    print(b3.id)
    b4 = Base(5)
    print(b4.id)
    b5 = Base()
    print(b5.id)
    b6 = Base()
    print(b6.id)
