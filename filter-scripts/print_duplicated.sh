#!/bin/bash

# define the file path variable
file_path="/var/lib/awx/projects/we/logs/iosxr/10.100.100.53/test.log"

# use while loop to read the file line by line
while read line; do

  # check if the line contains the target word
  if [[ $line == *"RP/0/RP0/CPU0"* ]]; then

    # print the line containing the target word
    echo "$line"

    # print the contents between the target word
    sed -n "/RP\/0\/RP0\/CPU0/,/RP\/0\/RP0\/CPU0/ { /RP\/0\/RP0\/CPU0/!p; }" <<< "$line"
    
  fi

done < "$file_path"

