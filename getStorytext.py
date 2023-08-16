# import required module
import os
from pathlib import Path; 
# assign directory
directory = '_posts'

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start


for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        file1 = open(f, 'r')
        Lines = file1.readlines()
        file1.close()

        count = 0
        # Strips the newline character
        file1 = open("../piper/" + os.path.splitext(Path(f).stem)[0] + ".txt", 'w')
        print()
        for line in Lines:
            count += 1
            if count > 10:
                print("{}".format(line.strip()))
                file1.write(line)
        file1.close()
