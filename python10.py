"""
#
# Part" Python JSON
# API = Application Programing Inter
# 
"""

import json

x = '{"name": "Jimmy", "age": "21", "city": "Phuket"}'

y = json.loads(x)

print(y)
print(type(y))
print(y["city"])

a = {
    "name": "Noa",
    "age": 20,
    "city": "Phuket"
}

b = json.dumps(a)

print(b)