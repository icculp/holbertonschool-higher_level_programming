#!/usr/bin/python3
a = 5
print(id(a))
a = 6
print(id(a))
b = 5
print(id(b))
b = 6
print(id(b))
print(a is b)
print("--------")
a = "HBTN"
b = "HBTN"
c = "hbtn"
print(id(a))
print(id(b))
print(id(c))
del a
print(id(b))
del b
c = "HBTN"
print(id(c))
