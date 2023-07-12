#!/usr/bin/python3
"""
Script: 7-add_item
Adds all arguments to a Python list and saves them to a file
"""

import sys
import os

# Import the required functions from the respective modules
save_to_json_file(my_obj, filename) = __import__('5-save_to_json_file').save_to_json_file(my_obj, filename)
load_from_json_file(filename) = __import__('6-load_from_json_file').load_from_json_file(filename)

# Create a list to store the data
data_list = []

# Check if the file exists and load the data if it does
if os.path.exists("add_item.json"):
    data_list = load_from_json_file(filename)("add_item.json")

# Add the command-line arguments to the list
for arg in sys.argv[1:]:
    data_list.append(arg)

# Save the list to a file using JSON representation
save_to_json_file(my_obj, filename)(data_list, "add_item.json")

