#!/usr/bin/python3

"""Write a function that reads a text file (UTF8) and prints it to stdout:"""

def read_file(filename=""):

    """This function reads the file content"""


    with open(filename, "r", encoding="UTF-8") as myfile:

        print(myfile.read(), end="")
        

