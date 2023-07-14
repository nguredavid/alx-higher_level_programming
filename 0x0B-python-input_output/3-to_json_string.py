#!/usr/bin/python3
import json
'''Write a function that returns the JSON representation of an object (string):'''

def to_json_string(my_obj):

    
    my_obj_json = json.dumps(my_objs)
    return my_obj_json

'''call function'''
my_objs = ['david', {'marks': (20, 30, 50, 80)}]
outcome = to_json_string(my_objs)

print(outcome)
