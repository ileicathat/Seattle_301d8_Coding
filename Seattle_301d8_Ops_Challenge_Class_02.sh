#!/bin/bash

# Script: Ops 301 Class 02 Ops Challenge
# Author: Justin R. Dotson
# Date of latest revision: 05-31-23
# Purpose: Ops Challenge - Time and date stamp logging
        # Overview
        

        
#Get the current date and time
current_date_log=$(date +"%Y-%m-%d_%H:%M:%S")

#Set the destination filename with the current date and time appended
destination_filename="systemlog_${current_date_log}.log"

#Copy /var/log/syslog to the current working directory with the new filename
cp /var/log/syslog "$destination_filename"

#Display a message with the name of the copied file
echo "Copied /var/log/syslog to $destination_filename"