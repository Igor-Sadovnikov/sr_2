import json
import requests

out = set()
with open('fraud.json') as json_file:
    data = json.load(json_file)
    server = data['server']
    port = data['port']
    sp = data['from_gold']
print(server)
print(port)
response = requests.get(f'http://{server}:{port}')
json_response = response.json()
# json_response = json_response.decode('utf-8')
print(json_response)
sp_serv = []
for elem in json_response:
    names = elem['name']
    founds = elem['found']
    sp_serv.append(tuple([names, founds]))
for elem in sp_serv:
    for line in sp:
        if line in elem[1]:
            out.add(elem[0])
out = sorted(list(out))
print(*out, sep='; ')