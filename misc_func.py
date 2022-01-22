"""
Randomizer: Misc Functions
Python 3.9
1/19/2022
Dane Burchette
"""

import csv
from os import system, name

def load_csv(csvfilename, single_dict=False):
    """Load Data from CSV file as list of dictionaries"""
    _list = []
    with open(csvfilename, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            _list.append(row)
    if single_dict:
        # Return only the first dictionary
        return _list[0]
    else:
        return _list

def save_csv(csvfilename, list_of_dict, fieldnames):
    """Save updated csv file"""
    with open(csvfilename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in list_of_dict:
            writer.writerow(row)

def load_keys(list_of_dict, single_dict=False):
    """Generate list of keys for csv dictionaries"""
    if not single_dict:
        list_keys = list(list_of_dict[0].keys())
    else:
        list_keys = list(list_of_dict.keys())
    return list_keys

def _clear_screen():
    """Clear screen"""
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

