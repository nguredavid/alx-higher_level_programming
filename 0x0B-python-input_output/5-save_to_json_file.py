#!/usr/bin/python3

'''Write a function that writes an Object to a text file, using a JSON representation:'''

def save_to_json_file(my_obj, filename):

    with open(my_obj, 'w', unicoding = 'UTF-8') as myfile:

        result = myfile.write(filename)
        return result
res = save_to_json_file('text.txt')
print(res)
