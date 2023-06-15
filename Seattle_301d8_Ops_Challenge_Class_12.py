# START CODE

#!/usr/bin/env python3

# seattle-ops-301d8
# Ops Challenge: Python Requests Library
# Overview
# Ever wondered how web browsers like Google Chrome communicate with web servers to create the interactive web sites and apps we use every day? One technical answer is HTTP requests. Today, you will be performing HTTP GET requests using the requests Python library. This library is very useful for a security professional to evaluate how a web server responds to outside requests.

# Resources
# Python Requests Library Guide
# Objectives
# Create a Python script that performs the following:

# Prompt the user to type a string input as the variable for your destination URL.

# Prompt the user to select a HTTP Method of the following options:
# GET
# POST
# PUT
# DELETE
# HEAD
# PATCH
# OPTIONS
# Print to the screen the entire request your script is about to send. Ask the user to confirm before proceeding.

# Using the requests library, perform a request against the destination URL with the HTTP Method selected by the user.

# For the given header, translate the codes into plain terms that print to the screen; for example, a 404 error should print Site not found to the terminal instead of 404.

# For the given URL, print response header information to the screen.

# Stretch Goals (Optional Objectives)
# Pursue stretch goals if you are a more advanced user or have remaining lab time.

# Have your script perform authentication into api.github.com using the auth command.

# Add timeouts to your script.

# Add error handling to your script.

#!/usr/bin/env python3

# First you'll need to install the requests library to your system
# Next, like any library, import it into your Python script
#import requests

# Assign a requests.get function to a variable. Be sure to pass a parameter (the URL) into the function for it to work.
response = requests.get('https://api.github.com')

# Print the status code obtained by the function using [var name].status code
#print(response.status_code)

# This will return status code 200. Look it up at https://developer.mozilla.org/en-US/docs/Web/HTTP/Status


# START CODE

#!/usr/bin/env python3

import os 
import requests

# Prompt the user for destination URL
url = input("Enter the destination URL including https://: ")

# Prompt the user to select HTTP Method
http_method = input("Select an HTTP Method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ")

# Print the request information
print(f"Sending {http_method} request to: {url}")

# Ask for user confirmation
confirmation = input("Press 'Y' to confirm and proceed: ")

if confirmation.lower() != 'y':
    print("Request canceled.")
else:
    # Perform the request
    if http_method.upper() == 'GET':
        response = requests.get(url)
    elif http_method.upper() == 'POST':
        response = requests.post(url)
    elif http_method.upper() == 'PUT':
        response = requests.put(url)
    elif http_method.upper() == 'DELETE':
        response = requests.delete(url)
    elif http_method.upper() == 'HEAD':
        response = requests.head(url)
    elif http_method.upper() == 'PATCH':
        response = requests.patch(url)
    elif http_method.upper() == 'OPTIONS':
        response = requests.options(url)
    else:
        print("Invalid HTTP Method.")
        exit()

    # Print the response status code
    print(f"Response Status Code: {response.status_code}")