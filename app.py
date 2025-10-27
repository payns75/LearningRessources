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

import sys

for path in sys.path:
    print(path)

# sys.path.append('.\\test\\')
# from pricing import get_net_price as calculate_net_price

import test
print(test.TAX_RATE)
print(test.tax(100, test.TAX_RATE))
test.plop()

# from test.pricing import get_net_price
# net_price = get_net_price(
#     price=100,
#     tax_rate=0.1,
#     discount=0.05
# )
# print(net_price)