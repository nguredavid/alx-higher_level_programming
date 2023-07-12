#!/usr/bin/python3

'''define a function called append_write'''
def append_write(filename="", text=""):

    '''supposed to append a string at the end of the text'''

    with open(filename, 'a', encoding='UTF-8') as myfile:

        characters = myfile.write(text)

        return characters



