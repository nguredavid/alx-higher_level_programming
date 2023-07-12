#!/usr/bin/python3

'''Write a function that reads a text file (UTF8) and prints it to stdout:'''

def read_file(filename=""):

    with open('filename', 'r', encoding='utf-8') as myfile:

        content = myfile.read()
        print(content)
'''call the function'''
read_file(example.txt)
