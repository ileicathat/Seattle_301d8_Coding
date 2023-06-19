

# Script: Ops 301 Class 04 Ops Challenge
# Author: Justin R. Dotson
# Date of latest revision: 06-02-23
# Purpose: Ops Challenge - Objectives
# Create a bash script that launches a menu system with the following options:



#!/bin/bash

# while true; do
#     clear
#     echo "Do you like people or computers, or something else?"
#     echo "1. People"
#     echo "2. Computers"
#     echo "3. Other"
#     echo "4. Exit"
#     read choice

#     if [[ $choice == 1 ]]; then
#         echo "People are cool"
#         # The -p option is used with the read command to display a prompt to the user and wait for them to enter input.
#         read -p "Press Enter to continue"
#     elif [[ $choice == 2 ]]; then
#         echo "Computers are great"
#         read -p "Press Enter to continue"
#     elif [[ $choice == 3 ]]; then
#         echo "Oh, you are not a people or computer person!"
#         read -p "What is your friend of choice? " friend
#         echo "I like $friend too!"
#         read -p "Press Enter to continue"
#     elif [[ $choice == 4 ]]; then
#         echo "See ya later!"
#         exit 0
#     else
#         echo "Invalid choice"
#         read -p "Press Enter to continue"
#     fi
# done


#!/bin/bash

print_menu() {
    echo "Menu:"
    echo "1. Hello world"
    echo "2. Ping self"
    echo "3. IP info"
    echo "4. Exit"
}

action_hello_world() {
    echo "Hello world!"
}

action_ping_self() {
    ping -c 4 127.0.0.1
}

action_ip_info() {
    ifconfig
}

while true; do
    print_menu
    read -p "Enter your choice: " choice

    case $choice in
        1)
            action_hello_world
            ;;
        2)
            action_ping_self
            ;;
        3)
            action_ip_info
            ;;
        4)
            echo "Exiting..."
            break
            ;;
        *)
            echo "Invalid choice. Please try again."
            ;;
    esac

    echo
done
