#!/bin/bash

directory_name="new_directory"

# Create the directory
mkdir "$directory_name"

# Change to the newly created directory
cd "$directory_name" || exit

# Create five empty files
for ((i=1; i<=5; i++))
do
    touch "file$i.txt"
done

echo "New directory '$directory_name' created with 5 empty files."
