#!/usr/bin/python3

'''Write a script that adds all arguments to a Python list, and then save them to a file:'''

import json
import sys

def save_to_json_file(my_obj, filename):

    with open(filename, 'w', encoding = 'UTF-8') as myfile:

       json.dump(my_obj, myfile)

def load_from_json_file(filename):

    with open(filename, 'r', encoding = 'UTF-8') as myfile:

        return json.load(myfile)

'''load existing file from the data'''
try:
    existing_data = load_from_json_file('output.json')
except FileNotFoundError:
    existing_data = []

'''add new arguments to the data_list'''
new_data = sys.argv[1:]
existing_data.extend(new_data)

'''save updated_data list'''

save_to_json_file(existing_data, 'output.json')
