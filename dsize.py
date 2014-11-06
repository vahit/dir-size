#!/usr/bin/env python

#############################################################
# FileName =  dsize.py                                      #
# Descriprion = Calcualte a Directory Size and return that. #
# FeedBack = Vahid.Maani@gmail.com                          #
#############################################################

# Import Needed Modules
import os
import sys

# Define needed variables
file_list = []
size = 0

# Check usage.
if len(sys.argv) < 2:
    print("You should specify a directory like this:")
    print("\tdir_size.py <directory>")
    sys.exit()

# Fine files list.
for dirpath, dirs, files in os.walk(sys.argv[1]):
    for filename in files:
        if not filename.startswith("."):
            file_list.append(os.path.join(dirpath, filename))

# Find files size and calculate their sum.
for x in file_list:
    size += os.path.getsize(x)

unit_list = ["B", "K", "M", "G"]
unit = 0

while (size > 1020) and (unit < 4):
    size /= 1024
    unit += 1

print(str(round(size,1))+unit_list[unit])
