#!/usr/bin/python3
'''5-text_indentation'''


def text_indentation(text):
    '''Prints some text with two lines after ? . or :'''
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.strip()
    flag = 0
    for char in text:
        if char in '?.:':
            print(char)
            print()
            flag = 1
        elif flag is 1 and char is ' ':
            flag = 0
            pass
        else:
            print(char, end='')
