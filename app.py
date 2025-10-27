person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}

print(person.get('ssn', '000-000-000'))

person['gender'] = 'male'

print(person.items())

empty_set = set()

from functools import partial

def multiply(a, b):
    return a*b


double = partial(multiply, b=3)


try:
    10 / 0
except ZeroDivisionError as e:
    print(f"Caught an error: {e}")

result = double(10)
print(result)

import csv

with open('country.csv', encoding="utf8") as f:
    csv_reader = csv.reader(f)
    for line_no, line in enumerate(csv_reader, 1):
        if line_no == 1:
            print('Header:')
            print(line)  # header
            print('Data:')
        else:
            print(line)  # data