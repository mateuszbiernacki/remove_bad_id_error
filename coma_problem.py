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
    text = re.split('SENTE-KADRY', buff)
    print(text)
    buff = re.sub(';\n', ';\n&', text[1])
    buff = re.sub(',,', '@', buff)
    buff = re.sub(',', '!', buff)
    buff = re.sub('\n&!', '\n', buff)
    buff = re.sub('@', ',', buff)
    buff = re.sub('!', ',,', buff)
    buff = re.sub('\n&', '\n,', buff)
    new_file = text[0] + 'SENTE-KADRY' + buff
    file = open('data_to_edit/' + filename, 'w')
    file.write(new_file)
print(i)
