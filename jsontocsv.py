"""
'PREREQUISITES'
* It is easiest to keep this code and the desired files in the same folder
(If not, just make sure to indicate the right, and same, path for both json and csv file)
* I didn't provide the file with command line arguments, therefore the 2022 should be manually changed

To run, just type 'python3 jsontocsv.py' in the command line :)
"""

import json
import csv
 
with open('2022.json') as json_file:
    jsondata = json.load(json_file)
 
data_file = open('2022.csv', 'w', newline='')
csv_writer = csv.writer(data_file)
 
count = 0
for data in jsondata:
    if count == 0:
        header = data.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(data.values())
 
data_file.close()