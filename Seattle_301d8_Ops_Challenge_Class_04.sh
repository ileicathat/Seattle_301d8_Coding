#!/bin/bash

# Script: Ops 301 Class 04 Ops Challenge
# Author: Justin R. Dotson
# Date of latest revision: 06-02-23
# Purpose: Ops Challenge - Objectives
# Create a bash script that launches a menu system with the following options:
# Hello world (prints “Hello world!” to the screen)
# Ping self (pings this computer’s loopback address)
# IP info (print the network adapter information for this computer)
# Exit
# Next, the user input should be requested.
# The program should next use a conditional statement to evaluate the user’s input, then act according to what the user selected.
# Use a loop to bring up the menu again after the request has been executed.




while true; do
    clear
    echo "Do you like people or computers, or something else?"
    echo "1. People"
    echo "2. Computers"
    echo "3. Other"
    echo "4. Exit"
    read choice

    if [[ $choice == 1 ]]; then
        echo "People are cool"
        # The -p option is used with the read command to display a prompt to the user and wait for them to enter input.
        read -p "Press Enter to continue"
    elif [[ $choice == 2 ]]; then
        echo "Computers are great"
        read -p "Press Enter to continue"
    elif [[ $choice == 3 ]]; then
        echo "Oh, you are not a people or computer person!"
        read -p "What is your friend of choice? " friend
        echo "I like $friend too!"
        read -p "Press Enter to continue"
    elif [[ $choice == 4 ]]; then
        echo "See ya later!"
        exit 0
    else
        echo "Invalid choice"
        read -p "Press Enter to continue"
    fi
done