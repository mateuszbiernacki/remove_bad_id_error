import os
import json
import re

companies_file = open("input/nums.json")
json_data = json.loads(companies_file.read())
path = 'data_to_edit'
i = 0
for filename in os.listdir(path):
    i += 1
    file = open('data_to_edit/' + filename, 'r')
    buff = file.read()
    file.close()
    year = re.sub(r'^(.*)\n(.*)\n', "", buff)[0:4]
    if year == "2020":
        if json_data[filename[0:4]][0] == -1:
            print(f'ERROR {filename}')
            new_file = buff
        else:
            new_file = str(json_data[filename[0:4]][0]) + ';' + re.sub(r'^(.*);', "", buff)
    elif year == "2021":
        if json_data[filename[0:4]][1] == -1:
            print(f'ERROR {filename}')
            new_file = buff
        else:
            new_file = str(json_data[filename[0:4]][1]) + ';' + re.sub(r'^(.*);', "", buff)

    file = open('data_to_edit/' + filename, 'w')
    file.write(new_file)


print(i)