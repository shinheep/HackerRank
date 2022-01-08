# Task
# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

# Function Description
# Complete the split_and_join function in the editor below.

# split_and_join has the following parameters:
# string line: a string of space-separated words

def split_and_join(line):
    a = line.split(" ")
    b = "-".join(a)
    return(b)
