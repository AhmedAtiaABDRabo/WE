#!/bin/bash


##########################
#       FUNCTION         #
##########################
#This script searches for word "msg" and prints all lines until it founds the word "2023"

#This script is used to filter output from the ansible.log file into log files for playbooks.



#BEGIN SCRIPT


# Enter the filename and word to search for
filename="ansible.log"
search_word=""msg""

# Find the line number(s) containing the search word
line_numbers=$(grep -n "$search_word" "$filename" | cut -d ":" -f 1)

# Loop through each line number and print all lines after the search word until the character 2023
for line_number in $line_numbers; do
  echo "----------"
  sed -n "$((line_number-1))p" "$filename" | awk -F '|' '{print $2}'
  # Print all lines after the search word until the character 2023
  sed -n "${line_number},/}/p" "$filename" | tail -n +1
done
