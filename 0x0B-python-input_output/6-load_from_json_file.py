#!/usr/bin/python3

'''Write a function that creates an Object from a “JSON file”:'''

import json

'''define a function'''
def load_from_json_file(filename):

    with open(filename, 'r', encoding = 'UTF-8') as myfile:

       return json.load(myfile)

'''create data'''
data = load_from_json_file('output.json')

print(data)

