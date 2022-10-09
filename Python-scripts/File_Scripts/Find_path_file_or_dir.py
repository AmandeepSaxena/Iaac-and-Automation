
from genericpath import isfile
import os


path = input("Enter your path: ")
if os.path.exists(path):
    print(f'Given path is valid path {path}')
    if os.path.isfile(path):
        print(f'Given path: {path} is file')
    else: 
        print(f'Given path: {path} is directory')
else:
    print(f'Please enter valid path and try again...')