#!/usr/bin/python3
import json
'''Write a function that writes an Object to a text file, using a JSON representation:'''

def save_to_json_file(my_obj, filename):

    with open(filename, 'w', encoding = 'UTF-8') as myfile:

        json.dump(my_obj, myfile)
'''create object'''
data_list= [
    ["David", {"marks": (30, 50, 100)}],
    ["Hudson", {"marks": (940, 70, 90)}],
    ["Millicent", {"Marks": (50, 60, 80)}]
]
save_to_json_file(data_list, 'output.json')
