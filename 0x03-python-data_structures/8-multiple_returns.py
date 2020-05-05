#!/usr/bin/python3
def multiple_returns(sentence):
    if (len(sentence) == 0):
        ls = 0
        fc = None
    else:
        ls = len(sentence)
        fc = sentence[:1]
    poople = (ls, fc)
    return (poople)
