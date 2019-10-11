import csv
import json


# - Reading a CSV
'''
with open('data/deniro.csv') as csv_file:
    file_reader = csv.reader(csv_file)
    for row in file_reader:

        print(row)
'''
# Read a json file

with open('data/sample.json') as json_file:
    data = json.load(json_file)
    # print(data['students'])
    # print(data)
    # print(json.dumps(data, indent=4))
    for student in data['students']:
        print('Student Name: ' + student['name'] +
              ', Student Age: ' + str(student['age']))


# Homework -- APIs (Cardi B; Ed Sheeran)
