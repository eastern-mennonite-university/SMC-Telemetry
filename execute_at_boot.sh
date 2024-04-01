#!/bin/bash

# Read the email addresses from the text file
IFS=',' read -ra ADDR < emails.txt

# Email settings
SUBJECT="Shell Marathon, onboard PI rebooted"
WELCOME_MSG="The onboard PI is ON and rebooted\n\n"

# Get system information
IFCONFIG_INFO=$(ifconfig)
CPU_INFO=$(lscpu)
STORAGE_INFO=$(df -h)

# Loop through the email addresses and send an email to each one
for i in "${ADDR[@]}"; do
        MESSAGE="${WELCOME_MSG}${IFCONFIG_INFO}\n\n${CPU_INFO}\n\n${STORAGE_INFO}"
        echo -e "$MESSAGE" | mail -s "$SUBJECT" "$i"
done
