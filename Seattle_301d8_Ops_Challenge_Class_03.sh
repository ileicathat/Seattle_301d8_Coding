#!/bin/bash

# Script: Ops 301 Class 02 Ops Challenge
# Author: Justin R. Dotson
# Date of latest revision: 05-31-23
# Purpose: Ops Challenge - Time and date stamp logging
        # Overview
        #!/bin/bash

# Prompt user for input directory path
read -p "Enter the directory path: " directory

# Prompt user for input permissions number
read -p "Enter the permissions number: " permissions

# Navigate to the directory
cd "$directory" || { echo "Failed to navigate to directory. Exiting."; exit 1; }

# Change permissions of all files in the directory
chmod -R "$permissions" *

# Print directory contents and permissions
echo -e "\nDirectory contents:"
ls -l
