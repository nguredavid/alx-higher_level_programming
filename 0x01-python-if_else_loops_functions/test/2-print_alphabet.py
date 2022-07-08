#!/usr/bin/python3
import string
for alpha_letters in string.ascii_lowercase:
    if alpha_letters not in 'eq':
        print(f'{alpha_letters}', end='')
