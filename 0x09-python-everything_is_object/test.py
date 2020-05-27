#!/usr/bin/python3
l1 = [1, 2, 3]
l2 = l1
print(id(l1))
print(id(l2))
l2[1] = 98
l1[0] = 89
print(l1)
print(l2)
l1 += [4]
l2[1] = 100
l1[0] = 111
print(id(l1))
print(id(l2))
print(l1)
print(l2)

a = [1, 2, 3]
print(id(a))
a += [4]
print(id(a))


'''
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
print(id(c))'''
