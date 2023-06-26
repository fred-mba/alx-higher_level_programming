#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
words = str.split()  # Split the string into a list of words
str = " ".join([words[5], words[6], words[7], words[0]])  # Concatenate the desired words
print(str)
