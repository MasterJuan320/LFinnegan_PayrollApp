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


salary_dict = {}

with open(INPUT_PPSN_CSV_FILE, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        ppsn = row['PPSN']
        name = row['Name']
        person_dict = salary_dict.get(row['PPSN'], {})
        person_dict['name'] = name
        salary_dict[ppsn] = person_dict