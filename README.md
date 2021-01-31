# README

This was a quick project completed to increase productivity. 

As a TA, when I complete marking, I need to download a directory containing a subdirectory for each student's assignment from the school's LMS.
On the LMS submissions are sorted alphabetically, thus marks are entered in alphabetical order. However, the naming format for the downloaded subdirectories is such that student's names are in the middle of the name, therefore the directories cannot be sorted by last name. 
When marking, a significant amount of time is wasted scanning the directories to find the next submission to mark. This was the motivation for creating a simple script to rename the directories so that they can be sorted by last name!

A simple Python script to rename subdirectories within directories downloaded from BrightSpaces
Student last names will be appended to the start of the directory name to allow sorting alphabetically by last name
 
Designed to be used in conjuction with rename.bat
 
# Instructions:
 1. Unzip the directory downloaded from BrightSpaces
 2. Place the unzipped directory into the directory containing sort_by_last_name.py and rename.bat
 3. Drag and drop the unzipped directory onto rename.bat
 4. Script supports processing multiple directories (drag and drop multiple unzipped directories together in step 3)
  
