import json
from pprint import pprint

with open('students.json') as f:
    data = json.load(f)

pprint(data)
