import json
import requests

out = set()
with open('fraud.json') as json_file:
    data = json.load(json_file)
    server = data['server']
    port = data['port']
    sp = data['from_gold']
# print(server)
# print(port)
# response = requests.get(f'http://{server}:{port}')
# json_response = json.loads(response.text)
# print(json(response.text))
# json_response = response.json()
# json_response = json_response.decode('utf-8')
# print(json_response)
with open('fraud1.json') as json_file:
    data = json.load(json_file)
    for elem in data:
        for line in sp:
            if line in elem['found']:
                out.add(elem['name'])
out = sorted(list(out))
print(*out, sep='; ')