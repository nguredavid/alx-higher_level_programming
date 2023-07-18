#!/usr/bin/python3
import json
'''Write a function that writes an Object to a text file, using a JSON representation:'''

def save_to_json_file(my_obj, filename):

    with open(filename, 'w', encoding = 'UTF-8') as myfile:

        json.dump(my_obj, myfile)
'''create object'''
data = ["David", {"marks": (30, 50, 100)}]
save_to_json_file(data, 'output.json')
