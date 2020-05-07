#!/usr/bin/python3
multiply_by_2 = __import__('9-multiply_by_2').multiply_by_2
print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = {'John': -2, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
#{'John': -2, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16
#                , 'sdfadsfa': 1, 'asdfasdfb': 2, 'asdfasdfc': '3', 'asdfdfd': 4
#                , 'asdfae': 5, 'dsadfsaff': 6, 'hejhrukg': 7, 'opjqwpofjh': 8}
new_dict = multiply_by_2(a_dictionary)
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)
