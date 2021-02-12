import os
import io

def file_formatting (path:str):
    with open(path,'r') as f:
        print (f.read())

print(file_formatting(path='tests/testfiles/test.txt'))
