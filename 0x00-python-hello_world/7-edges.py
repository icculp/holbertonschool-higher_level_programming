#!/usr/bin/python3
word = "Holberton"
word_first_3 = {:3}.format(word)
word_last_2 = {:-2}.format(word)
middle_word = {1:8}.format(word)
print("First 3 letters: {}".format(word_first_3))
print("Last 2 letters: {}".format(word_last_2))
print("Middle word: {}".format(middle_word))
