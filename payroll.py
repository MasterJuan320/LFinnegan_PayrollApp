""" Payroll Management System
 Liam Finnegan
"""



import os
import csv

CURRENT_DIRECTORY = os.path.dirname((__file__))
INPUT_PPSN_CSV_FILE = os.path.join(CURRENT_DIRECTORY, 'Input', 'PPSN.csv')
INPUT_BENIFITS_CSV_FILE = os.path.join(CURRENT_DIRECTORY, 'Input', 'benefits.csv')
INPUT_BONUSES_CSV_FILE = os.path.join(CURRENT_DIRECTORY, 'Input', 'bonuses.csv')
INPUT_RATE_CSV_FILE = os.path.join(CURRENT_DIRECTORY, 'Input', 'rates.csv')
INPUT_TIMETABLE_CSV_FILE = os.path.join(CURRENT_DIRECTORY, 'Input', 'hours.csv')


def read_csv(filename, dict_update, field_name):
    """
    Docstring for read_csv
    
    :param filename: Description
    :param dict_update: Description
    :param field_name: Description
    """
    with open(filename, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            ppsn = row['PPSN']
            field = row[field_name]
            person_dict = dict_update.get(row['PPSN'], {})
            person_dict[field_name] = field
            dict_update[ppsn] = person_dict

salary_dict = {}

read_csv(INPUT_PPSN_CSV_FILE, salary_dict, 'Name')
read_csv(INPUT_BENIFITS_CSV_FILE, salary_dict, 'Benefits')
read_csv(INPUT_BONUSES_CSV_FILE, salary_dict, 'Bonuses')
read_csv(INPUT_RATE_CSV_FILE, salary_dict, 'Rate')
read_csv(INPUT_TIMETABLE_CSV_FILE, salary_dict, 'Hours')

print(salary_dict)
