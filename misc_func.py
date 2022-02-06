"""
Randomizer: Misc Functions
Python 3.10.2
1/19/2022
Dane Burchette
"""

import csv
from os import system, name

def load_csv(csvfilename, single_dict=None):
    """Load Data from CSV file as list of dictionaries"""
    _list = []
    with open(csvfilename, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            _list.append(row)
    match single_dict:
        case True:
            # Return only the first dictionary
            return _list[0]
        case _:
            return _list

def save_csv(csvfilename, list_of_dict, fieldnames):
    """Save updated csv file"""
    with open(csvfilename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in list_of_dict:
            writer.writerow(row)

def load_keys(list_of_dict, single_dict=None):
    """Generate list of keys for csv dictionaries"""
    match single_dict:
        case True:
            list_keys = list(list_of_dict.keys())
        case _:
            list_keys = list(list_of_dict[0].keys())
    return list_keys

def _clear_screen():
    """Clear screen"""
    match name:
        case 'nt':
            _ = system('cls')
        case _:
            _ = system('clear')