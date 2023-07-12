#!/usr/bin/python3
'''write a file'''

with open('text.py', 'w', encoding='utf-8') as myfile:

    myfile.write('Just learning here\n')

'''read the file'''
with open('text.py', 'r', encoding='utf-8') as myfile:

    print(myfile.read())

