#!/usr/bin/env python3

# Import libraries

import os

# Declaration of variables

### Read user input here into a variable


# Declaration of functions

def generate_directory(directory_path):
    for (root, dirs, files) in os.walk(directory_path):
        print("==root==")
        print(root)
        print("==dirs==")
        print(dirs)
        print("==files==")
        print(files)

# Main
user_input = input("Enter the directory path: ")
generate_directory(user_input)

# End