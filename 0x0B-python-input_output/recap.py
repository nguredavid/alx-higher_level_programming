#!/usr/bin/python3
import json
'''Write a function that writes an Object to a text file, using a JSON representation:'''

def save_to_json_file(my_obj, filename):

    with open(filename, 'w', encoding = 'UTF-8') as myfile:
        json.dump(my_obj, myfile)
        

data = ["David", {"marks": (20, 30, 50)}]        
save_to_json_file(data, 'text.txt')

