#!/usr/bin/python3
import json

'''Write JSON (Object) string to File'''

def json_file(my_ob, filename):
    with open(filename, 'w', encoding = "UTF-8") as myfile:
        res = json.dump(my_ob, myfile)
        return "File sucessfully written"


adict = {"name": "David", "age": 30}

output = json_file(adict, "print.json")

print(output)


