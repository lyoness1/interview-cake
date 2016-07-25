"""
Make a code that finds duplicate files. 
Return a tuple (copy, original) for each duplicate. 
Assume files are duplicated only once, and most recent is the copy.

"""

import os

def find_dupes(root):

    # initialize dict to track files that have been seen
    seen = {}

    # initialize stack to store files to be looked at
    to_check = [root]

    # initialize a list to store tuples of duplicates: (copy, original)
    dupes = []

    # loop until we've checked all the files in the root directory
    while to_check:

        # grab the top of the stack
        current = to_check.pop()

        # check if it's a directory or file
        # if directory, put contents in stack
        if os.path.isdir(current):
            for path in os.listdir(current):
                full_path = os.path.join(current, path)
                to_check.append(full_path)

        # if it's a file:
        else: 

            # get the contents
            with open(current) as file:
                file_contents = file.read()

            # get the most recent edit data
            last_edited = os.path.getmtime(current)

            # if we've seen it before
            if file_contents in seen:











