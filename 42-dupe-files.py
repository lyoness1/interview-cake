"""
Make a code that finds duplicate files. 
Return a tuple (copy, original) for each duplicate. 
Assume files are duplicated only once, and most recent is the copy.

"""

import os
import hashlib

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

            # get the contents HASH
            # use helper function (below): sample_hash_file
            file_hash = sample_hash_file(current)

            # get the most recent edit data
            last_edited = os.path.getmtime(current)

            # if it's a new file, add it to seen
            # record the path and last edited time
            if file_hash not in seen:
                seen[file_hash] = (last_edited, current)

            # OR, if we've seen the file before
            else:

                # get the existing path and edit time
                existing_last_edited, existing_path = seen[file_hash]

                # figure out which is the original vs. the copy
                # will be added to duplicates as (copy, original)
                if last_edited > existing_last_edited:
                    # current file is dupe! 
                    # leave existing file alone
                    dupes.append((current, existing_path))

                else:
                    # exisiting file is dupe! 
                    # delete existing file (by doing nothing with it)
                    dupes.append((existing_path, current))

                    # update seen to have the original in it
                    seen[file_hash] = (last_edited, current)

            return dupes





def sample_hash_file(path):
    """Uses the first, middle, and last few bytes to hash a file"""

    num_bytes_to_read = 4000
    total_bytes = os.path.getsize(path)

    hasher = hashlib.sha512()

    with open(path, 'rb') as file:

        # if the file is too short to take three, hash whole thing
        if total_bytes < num_bytes_to_read * 3:
            hasher.update(file.read())

        else:

            # math out how many bytes to skip between samples
            num_bytes_between_samples = (total_bytes - num_bytes_to_read*3) / 2

            # read, skip, read, skip, read
            for offset_multiplyer in xrange(3):
                start_of_sample = (offset_multiplyer
                    * (num_bytes_between_samples + num_bytes_to_read))
                file.seek(start_of_sample)
                sample = file.read(num_bytes_to_read)
                hasher.update(sample)   

    return hasher.hexdigest()



