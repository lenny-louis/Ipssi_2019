#!/usr/bin/python3

#count line
fname = "file.txt"
count = 0
with open(fname, 'r') as f:
    for line in f:
        count += 1
print("Total number of lines is:", count)
