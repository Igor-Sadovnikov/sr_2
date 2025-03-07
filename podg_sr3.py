import argparse
import requests
import json

parser = argparse.ArgumentParser()
parser.add_argument('host', nargs=1)
parser.add_argument('port', nargs=1)
parser.add_argument('dates', nargs='*')
parser.add_argument('--coeff', nargs='?', default=2, type=int)
parser.add_argument('--substract', nargs='?')
args = parser.parse_args()

response = requests.get(f'http://{args.host[0]}:{args.port[0]}')
json_response = response.json()
out = []
for key in json_response.keys():
    sp = json_response[key]
    count = 0
    if key in args.dates:
        for i in range(len(sp)):
            if sp[i] % 2 != 0:
                sp[i] *= int(args.coeff)
            else:
                if args.substract:
                    sp[i] = max(0, sp[i] - int(args.substract))
    summ = sum(sp)
    sr = summ / len(sp)
    for elem in sp:
        if elem < sr:
            count += 1
    out.append(tuple([key, summ, count]))
out = sorted(out, key=lambda x: x[0])
gen_sp = []
for elem in out:
    slov = {'date': elem[0], 'cost': elem[1], 'number': elem[2]}
    gen_sp.append(slov)

with open('outlay.json', 'w') as jsonfile:
    json.dump(gen_sp, jsonfile, ensure_ascii=False, indent=4)