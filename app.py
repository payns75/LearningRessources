import requests


class Person:
    
    def __init__(self, name):
        self.name = name
        self.counter = 0

    def greet(self):
        return f"Hello, {self.name}!"
    


# response = requests.get('https://www.google.com', verify=False)
# if response.status_code == 200:
#     print(response.text)

person = Person("Alice")
person.age = 30
print(person.name)

person.counter += 1
print(person.counter)