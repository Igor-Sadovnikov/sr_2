import argparse

parser = argparse.ArgumentParser()
parser.add_argument('host', nargs=1)
parser.add_argument('port', nargs=1)
parser.add_argument('dates', nargs='*')
parser.add_argument('--coeff', nargs='?', default=2)
parser.add_argument('--substract', nargs='?')
args = parser.parse_args()
with open('sr3.json') as jsonfile:
    