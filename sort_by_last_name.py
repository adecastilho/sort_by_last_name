#!/usr/bin/env python3

# Written by: Amanda de Castilho
# Date: January 29, 2021
#
# A simple script to rename subdirectories within directories downloaded from BrightSpaces
# Student last names will be appended to the start of the directory name to allow sorting alphabetically by last name
# 
# Designed to be used in conjuction with rename.bat
# 
# Instructions:
# 1. Unzip the directory downloaded from BrightSpaces
# 2. Place the unzipped directory into the directory containing sort_by_last_name.py and rename.bat
# 3. Drag and drop the unzipped directory onto rename.bat
# 4. Script supports processing multiple directories (drag and drop multiple unzipped directories together in step 3)
   
import os
import sys
from re import match

def main(argv):
	
	if len(argv) == 1:
		print("Argument error: you must drag one or more directories onto rename.bat")
		sys.exit()
	
	# sort each directory passed as cmd line arg
	
	for dir in argv[1:]:
		rename_subdirs(dir)

def rename_subdirs(dir):
	
    subdir_list = os.listdir(dir)
    
    for subdir in subdir_list:

        m = match(r"^\w*-\w*\s-\s\w*\s-\s\w*\s(?P<last_name>\w*).*", subdir)
        
        if m:
            old = dir + "/" + subdir
            new = dir + "/" + m["last_name"] + " - " + subdir
            os.rename(old, new)

if __name__ == '__main__':
    main(sys.argv)
