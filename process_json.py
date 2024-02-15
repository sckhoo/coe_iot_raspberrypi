import json
import datetime
import pytz
import csv

def process_json(data): 
# Iterating through the json
# list
    count = 0
    for i in data:
        #print(i)
        if i['data'].get('location') == "CM-CoE":
            count += 1
            try:
                dt_utc = datetime.datetime.fromtimestamp(i['timestamp']/1000)
                dt_local = dt_utc.astimezone(local_tz)
                dt_local = dt_utc.astimezone(local_tz)
                year = dt_local.year
                month = dt_local.month
                day = dt_local.day
                hour = dt_local.hour
                minute = dt_local.minute
                #print(f"timestamp (DD/MM/hh/mm): {month}:{day}:{hour}:{minute}, temperature: {i['data'].get('temperature')}, humidity: {i['data'].get('humidity')}")
                my_writer.writerow((month,day,hour,minute,i['data'].get('temperature'),i['data'].get('humidity')))

            except ValueError:
                print(i['timestamp'])
    print(f'Total data in {infile} is {count}')

input_files = ['09feb2024.json', '10feb2024.json', '11feb2024.json', '12feb2024.json', '13feb2024.json', '14feb2024.json']

local_tz = pytz.timezone("Asia/Kuala_Lumpur")

csvfile = open('cm_coe.csv', 'w', newline = '')
my_writer = csv.writer(csvfile, delimiter = ',')

for infile in input_files:
    # Opening JSON file
    f = open(infile)
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
    process_json(data)
    # Closing file
    f.close()
 
 
 
 
