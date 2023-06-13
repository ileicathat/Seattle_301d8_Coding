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

# Import the os module to handle file operations
import os

# Create a new .txt file
OpsChallenge10 = "Modifyme.txt"
file = open(OpsChallenge10, "w")

# Append three lines to the file
file.write("This Line First\n")
file.write("Second line\n")
file.write("Third line\n")

# Close the file
file.close()

# Read the first line from the file
file = open(OpsChallenge10, "r")
first_line = file.readline()
file.close()

# Print the first line to the screen
print("First line:", first_line)

# Delete the .txt file
os.remove(OpsChallenge10)