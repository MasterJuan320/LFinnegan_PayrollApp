""" Payroll Management System
 Liam Finnegan
"""



import os
import csv
import pprint

CURRENT_DIRECTORY = os.path.dirname((__file__))

INPUT_PPSN_CSV_FILE = os.path.join(CURRENT_DIRECTORY, 'Input', 'PPSN.csv', )
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

def calc_taxes(record_to_update):
    """Calculate the taxes for a given record.
    The taxes are calculated based on the salary + bonuses. If the total is less than 3000,
    the tax rate is 20%. If the total is 3000 or more,
    the tax rate is 40% over 3000.
    Parameters
    ----------
    record_to_update : dict
    The record to update with the calculated taxes.
    Returns
    -------
    None
    """
    salary_bonuses = record_to_update.get('Salary', 0) + record_to_update.get('Bonuses', 0)
    if salary_bonuses < 3000:
        record_to_update['Taxes'] = round(salary_bonuses * 0.2, 2)
    else:
        record_to_update['Taxes'] = round((salary_bonuses - 3000) * 0.4 + 3000 * 0.2, 2)



salary_dict = {}

read_csv(INPUT_PPSN_CSV_FILE, salary_dict, 'Name')
read_csv(INPUT_BENIFITS_CSV_FILE, salary_dict, 'Benefits')
read_csv(INPUT_BONUSES_CSV_FILE, salary_dict, 'Bonuses')
read_csv(INPUT_RATE_CSV_FILE, salary_dict, 'Rate')
read_csv(INPUT_TIMETABLE_CSV_FILE, salary_dict, 'Hours')

for ppsn, record in salary_dict.items():
    record['Salary'] = round(record.get('Hours', 0) * record.get('Rate', 0), 2)

for ppsn, record in salary_dict.items():
    calc_taxes(record)

pprint.pprint(salary_dict)
