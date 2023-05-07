#!/bin/bash

# Read the input file name from command line argument
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 input_file"
    exit 1
fi

input_file=$1

# Check if the input file exists
if [ ! -f "$input_file" ]; then
    echo "Input file $input_file does not exist"
    exit 1
fi

# Create a temporary file to store the formatted output
output_file=$(mktemp)

# Loop through each line of the input file
while read -r line; do
    # Trim leading and trailing whitespaces
    line=$(echo "$line" | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')

    # Prepend "RP/0/RP0/CPU0" to the line
    formatted_line="RP/0/RP0/CPU0 $line"

    # Append the formatted line to the output file
    echo "$formatted_line" >> "$output_file"
done < "$input_file"
