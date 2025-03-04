import csv
import json


sp = []
with open('people.csv', encoding = 'utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='_', quotechar='"')
    for elem in reader:
        if elem['event'] != elem['explanation'] and elem['benefit'] != '0':
            slov = {'name': elem['name'], 'event': elem['event'], 'benefit': elem['benefit']}
            sp.append(slov)


with open('dubious.json', 'w') as jsonfile:
    json.dump(sp, jsonfile, ensure_ascii=False, indent=4)
