"""
Given an aribitrary number of files, each of which contain one record per line.

Please write a command line program that will:

1. Take all the filesnames as arguments, and signal success if there are no duplicates between the files
2. Signal an error if there are any duplicates
3. For duplicates, print out the names of the duplicates and the files that contain the duplicate records

=== Sample data ===

$ cat egglayers
chicken
snake
alligator
platypus

$ cat winged
chicken
bat
eagle

$ cat warmblooded
chicken
platypus
human
seal
bat


=== Sample output ===

$ myscript ./egglayers ./winged ./warmblooded
chicken is in egglayers and winged and warmblooded
platypus is in egglayers and warmblooded
bat is in winged and warmblooded

"""

import sys
from collections import defaultdict

def find_duplicates(files):
    records = defaultdict(list)
    duplicates = defaultdict(list)
    

    for file in files:
        file = "Problems\\" + str(file)
        with open(file, 'r') as f:
            for line in f:
                record = line.strip()
                records[record].append(file)
                if len(records[record]) > 1:
                    duplicates[record] = records[record]

    if duplicates:
        for record, file_list in duplicates.items():
            print(f"{record} is in {' and '.join(file_list)}")
        sys.exit(1)
    else:
        print("No duplicates found.")
        sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: myscript <file1> <file2> ... <fileN>")
        sys.exit(1)

    find_duplicates(sys.argv[1:])