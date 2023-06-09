# # #!/usr/bin/env python3


# Ops Challenge: Python Collections
# Overview
# Python is known for its relevance to data science and consequently handles data quite well using array. A fundamental grasp of data structures and algorithms will help you a great deal in feeling comfortable with these concepts during an intense job interview for a position where you’ll be automating tedious processes for the company. Today, you will be working with lists in Python.

# Objectives
# Create a Python script that includes the following:

# Assign to a variable a list of ten string elements.
# Print the fourth element of the list.
# Print the sixth through tenth element of the list.
# Change the value of the seventh element to “onion”.
# Stretch Goals (Optional Objectives)
# Pursue stretch goals if you are a more advanced user or have remaining lab time.

# Use the below Python methods once each against your list to manipulate the elements in your list:

# append()
# clear()
# copy()
# count()
# extend()
# index()
# insert()
# pop()
# remove()
# reverse()
# sort()
# Create one tuple. Create one set. Create one dictionary.


# # # How to create and print a list

# # thislist = ["apple", "banana", "cherry"]
# # print(thislist)

# # # How to print the first item only

# # thislist = ["apple", "banana", "cherry"]
# # print(thislist[0])

# # # How to print the last item only by counting backwards

# # thislist = ["apple", "banana", "cherry"]
# # print(thislist[-1])

# # # How to print a range of elements in a list

# # thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# # print(thislist[2:5])

# # # How to print the beginning to a specific element number

# # thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# # print(thislist[:4])

# # # How to add an item to a list

# # # thislist = ["apple", "banana", "cherry"]
# # # thislist.append("orange")
# # # print(thislist)


# Start Main

import os


# Assign to a variable a list of ten string elements.

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", "lychee", "tomato", "blueberry"]


# Print the fourth element of the list.

print(thislist[3])

# Print the sixth through tenth element of the list.

print(thislist[5:])

# Change the value of the seventh element to “onion”.

(thislist[6])= "onion"
print(thislist)


# End


# Stretch Goals (Optional Objectives)