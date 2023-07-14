#!/usr/bin/python3

'''Write a function that returns an object (Python data structure) represented by a JSON string:'''

import json

def from_json_string(my_str):

   jstring = json.loads(my_str)
   return jstring

j_string = '{"marks": [30, 50, 70]}'

results = from_json_string(j_string)
print(results)
