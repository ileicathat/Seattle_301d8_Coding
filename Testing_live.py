#!/usr/bin/env python3


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

    # Translate status codes into plain terms
    status_codes = {
        200: "OK",
        201: "Created",
        204: "No Content",
        400: "Bad Request",
        401: "Unauthorized",
        403: "Forbidden",
        404: "Not Found",
        500: "Internal Server Error"
    }

    # Print the translated status
    if response.status_code in status_codes:
        print(f"Status: {status_codes[response.status_code]}")

    # Print response header information
    print("Response Headers:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")
