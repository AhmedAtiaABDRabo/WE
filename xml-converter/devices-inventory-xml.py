#!/bin/python3
import re

# Open the log file for reading
with open('/home/ansible/projects/we/logs/devices-inventory.log', 'r') as file:
    # Read the entire file into a string
    log_contents = file.read()

# Define a regular expression pattern to match text between double quotes
pattern = r'"([^"]*)"'

# Use the regular expression to find all matches in the log contents
matches = re.findall(pattern, log_contents)

# Define a function to convert a matched string into XML
def to_xml(match):
    return match

# Use the function to convert each match into XML
xml_strings = [to_xml(match) for match in matches]

# Write the XML strings to a new file
with open('devices-inventory.xml', 'w') as file:
    for xml_string in xml_strings:
        file.write(xml_string + '\n')
