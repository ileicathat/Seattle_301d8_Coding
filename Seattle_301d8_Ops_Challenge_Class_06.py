#!/usr/bin/env python3

import os

# Execute 'whoami' command
whoami_out = os.popen('whoami').read() #.strip()
print("Current user:", whoami_out)


# Execute 'ip a' command
ip_out = os.popen('ip a').read()
print("IP Address information:")
print(ip_out)

# Execute 'lshw -short' command
lshw_out = os.popen('lshw -short').read()
print("Hardware information:")
print(lshw_out)


# Execute 'pwd' command
pwd_output = os.popen('pwd').read()
print("Hardware information:")
print(pwd_output)

# Stretch Goals

import subprocess

# Execute a command and capture its output
result = subprocess.run(['ip', 'a'], capture_output=True, text=True)
print(result.stdout)  # Output: the result of 'ip a' command