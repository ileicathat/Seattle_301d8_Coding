#!/usr/bin/env python3

#DEMO CODE

# # Create a new file if it does not exist
# f = open("demofile.txt", "w")

# # How to open a file
# f = open("demofile.txt")

# # How to open a file and read it
# f = open("demofile.txt", "r")
# print(f.read())

# # How to return the five first characters of a file
# f = open("demofile.txt", "r")
# print(f.read(5))

# # Close a file when you're finished
# f = open("demofile.txt", "r")
# print(f.readline())
# 

# Start Code

# Create a new text file
file_path = "example.txt"
file = open(file_path, "w")

# Append three lines to the file
lines = ["First line", "Second line", "Third line"]
for line in lines:
    file.write(line + "\n")

# Close the file
file.close()

# Read the first line and print it
file = open(file_path, "r")
first_line = file.readline().rstrip()
print("First line:", first_line)

# Close the file
file.close()

# Delete the file
import os
os.remove(file_path)
