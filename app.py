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