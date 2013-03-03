#!/usr/bin/python3.3

import os
import sys

if len(sys.argv) < 2:
    print("You should specify a directory like this:")
    print("\tdir_size.py <directory>")
    sys.exit()

size_list = []

for dirpath, dirnames, filenames in os.walk(sys.argv[1]):
    for file_name in filenames:
        if dirpath != sys.argv[1]:
            break
        file_size = int(os.path.getsize(os.path.join(sys.argv[1],file_name)))
        size_list.append(file_size)

size = 0
for i in range(0,len(size_list)):
     size += size_list[i]
print(size)

unit_list = ["B", "K", "M", "G"]
unit = 0

while (size > 1020) and (unit < 4):
    size /= 1024
    unit += 1

print(str(round(size,1))+unit_list[unit])
