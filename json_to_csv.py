# 3. Write program that takes a JSON file as input and converts it to a CSV file.

# 3. Write program that takes a JSON file as input and converts it to a CSV file.

import json
import csv

def json_to_csv(json_file_path, csv_file_path):
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    with open(csv_file_path, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)



# json_to_csv(json_file_path, csv_file_path)