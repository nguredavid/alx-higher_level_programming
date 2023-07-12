#!/usr/bin/python3

"""Write a function that writes a string to a text file (UTF8) and returns the number of characters written:"""
"""defines a function called write_file"""
def write_file(filename="", text=""):
    """writes a file given"""

    with open(filename, "w", encoding="UTF-8") as myfile:

        characters = myfile.write(text)

        """returns the number of characters written"""

        return characters

        
'''call function'''

print(write_file("example.txt", "David"))


