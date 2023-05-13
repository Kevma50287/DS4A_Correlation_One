import os
import json

JSON_folder_path = './Json'
files = os.listdir(JSON_folder_path)
file = files[0]


with open(JSON_folder_path + "/" + file) as jsonFile:
    data = json.load(jsonFile)
    us_gaap = data['facts']['us-gaap']
    keys=[]
    formatted_data = {}
    formatted_data['entity_name'] = data['entityName']
    for key in us_gaap:
        keys.append(key)
        formatted_data[key] = us_gaap[key]

print(keys)