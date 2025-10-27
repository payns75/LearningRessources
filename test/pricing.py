# pricing.py
import test

def get_net_price(price, tax_rate, discount=0):
    discounted_price = price * (1 - discount) 
    net_price = discounted_price * (1 + tax_rate) 
    return net_price


def get_tax(price, tax_rate=0.07):

    return price * tax_rate * 2

print(__name__)