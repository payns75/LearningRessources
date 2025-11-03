class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f'Person({self.first_name},{self.last_name},{self.age})'

companies = [('Google', 2019, 134.81),
             ('Apple', 2019, 260.2),
             ('Facebook', 2019, 70.7)]
result = sorted(companies, key=lambda company: company[2], reverse=True)
print(companies)