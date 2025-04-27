#!/usr/bin/python3
import os
path = '/tmp/testfile.txt'
if os.path.isdir(path):
    print("The path is a Directory")
elif os.path.isfile(path):
    print("The Path contains file")
else:
    print("File or Directory Doesn't exists")


# For Linux