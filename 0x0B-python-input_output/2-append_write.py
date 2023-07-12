#!/usr/bin/python3

'''Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:'''

def append_write(filename="", text=""):

    '''supposed to append a string at the end of the text'''

    with open(filename, 'a', encoding='UTF-8') as myfile:

        characters = myfile.append(text)

        return characters



