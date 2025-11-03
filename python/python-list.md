# Python List

## Initier une liste

```python
empty_list = []
print(empty_list)
todo_list = ['Learn Python List','How to manage List elements']
print(todo_list)
numbers = [1, 3, 2, 7, 9, 4]
print(numbers)
coordinates = [[0, 0], [100, 100], [200, 200]]
print(coordinates)
```

## Accéder et modifier des éléments de liste

```python
numbers = [1, 3, 2, 7, 9, 4]
print(numbers[0]) # Premier élément de la liste
print(numbers[-1]) # Dernier élément de la liste
print(numbers[-2]) # Avant dernier élément de la liste

# Modifier un élément de la liste
numbers[0] = 10
print(numbers)
numbers[2] /= 2
print(numbers)
```

## Ajouter et modifier des éléments de liste

```python
numbers = [1, 3, 2, 7, 9, 4]
# Ajouter un élément
numbers.append(100)
print(numbers)
# Insérer un élément à une position
numbers.insert(2, 100)
print(numbers)
# Supprime un élément à une position
del numbers[0]
print(numbers)
# Supprime le dernier élément et le retourne
last = numbers.pop()
print(last)
print(numbers)
# Supprime le premier élément de la liste en fonction de sa valeur
numbers.remove(9)
```

## Ordonner une liste
```python
guests = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer']
guests.sort() # Ordre croissant
print(guests)
guests.sort(reverse=True) # Ordre décroissant
print(guests)
```

## Ordonner une liste de tuples
```python
companies = [('Google', 2019, 134.81),
             ('Apple', 2019, 260.2),
             ('Facebook', 2019, 70.7)]

# Version "classique"
def sort_key(company):
    return company[2]

companies.sort(key=sort_key, reverse=True)
print(companies)

# Avec une expression lambda
companies.sort(key=lambda company: company[2])
print(companies)
```

## Retourner une nouvelle liste ordonnée
```python
guests = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer']
sorted_guests = sorted(guests, reverse=True)
print(sorted_guests)
```

Retourne une nouvelle liste sans toucher à la liste source. Pour le reste fonctionne de la même façon que 'sort'.

```python
companies = [('Google', 2019, 134.81),
             ('Apple', 2019, 260.2),
             ('Facebook', 2019, 70.7)]
result = sorted(companies, key=lambda company: company[2], reverse=True)
print(companies)
```

## List slice

```python
sub_list = list[begin: end: step]
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
# Les éléments de 1 à 4
sub_colors = colors[1:4]
print(sub_colors)
# Les n premiers éléments
sub_colors = colors[:3]
print(sub_colors)
# Les n derniers éléments
sub_colors = colors[-3:]
print(sub_colors)
# Un élément sur 2
sub_colors = colors[::2]
print(sub_colors)
# Inverser une liste
reversed_colors = colors[::-1]
print(reversed_colors)
# Substituer une partie de la liste
colors[0:2] = ['black', 'white']
print(colors)
# Substituer une partie de la liste et insérer une nouvelle couleur 'gray'
colors[0:2] = ['black', 'white', 'gray']
print(colors)
# Supprimer des éléments de la liste
del colors[2:5]
print(colors)
```

## Unpack List
```python
# Affecte des varibales depuis une liste
## Il faut que la taille du tableau corresponde au nombre de variables à affecter.
colors = ['red', 'blue', 'green']
red, blue, green = colors
# On peut ajouter * pour mettre le reste du tableau.
colors = ['cyan', 'magenta', 'yellow', 'black']
cyan, magenta, *other = colors
print(cyan)
print(magenta)
print(other)
```

## Boucler dans une liste

```python
# Le plus simple pour boucler dans une liste
cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']
for city in cities:
    print(city)
# Ajouter l'index à l'énumération
# Cela retourne un tuple (Index, valeur)
for item in enumerate(cities):
    print(item)
# On peut unpack le tuple directement dans deux variables pour simplifier l'écriture.
for index, city in enumerate(cities):
    print(f"{index}: {city}")
# Il est possible de jouer sur la valeur du début de l'index directement dans la fonction d'énumération
for index, city in enumerate(cities,0):
    print(f"{index}: {city}")
```

## Trouver l'index d'un élément
```python
# Pour retrouver l'index d'un élément directement en recherchant par la valeur.
cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']

result = cities.index('Mumbai')
print(result)

# Note: Si la valeur n'existe pas dans la liste, alors retourne une erreur.
# Pour fixer cette partie, on peut faire le test avec le code suivant en utilisant in:
city = 'Osaka'

if city in cities:
    result = cities.index(city)
    print(f"The {city} has an index of {result}.")
else:
    print(f"{city} doesn't exist in the list.")
```

## Map pour transformer une liste

La fonction map est le plus souvent utilisée avec une expression lambda pour transformer le contenu d'une liste.

```python
# Utilisation de map:
iterator = map(fn, list)
# Exemple d'utilisation avec une expression lambda
bonuses = [100, 200, 300]
iterator = map(lambda bonus: bonus*2, bonuses)
```

Une fois que l'on a l'itérateur, on peut aller le lire en utilisant une boucle for ou en utilisant la fonction 'list'.

```python
names = ['david', 'peter', 'jenifer']
new_names = map(lambda name: name.capitalize(), names)
print(list(new_names))
```

On peut utiliser map avec ce que l'on veut. Par exemple ici, on va faire une opétation sur les tuples et ajouter une nouvelle valeur.

```python
carts = [['SmartPhone', 400],
         ['Tablet', 450],
         ['Laptop', 700]]
TAX = 0.1
carts = map(lambda item: [item[0], item[1], item[1] * TAX], carts)
print(list(carts))
```

## Filtrer sur une liste

La fonction filter est le plus souvent utilisée avec une expression lambda pour filtrer le contenu d'une liste.

```python
# Utilisation de filter:
filter(fn, list)
# Exemple de filtre, puis lecture de l'itérateur avec la fonction list():
scores = [70, 60, 80, 90, 50]
filtered = filter(lambda score: score >= 70, scores)
print(list(filtered))
```

Un autre exemple de filtre mais sur des tuples:

```python
countries = [
    ['China', 1394015977],
    ['United States', 329877505],
    ['India', 1326093247],
    ['Indonesia', 267026366],
    ['Bangladesh', 162650853],
    ['Pakistan', 233500636],
    ['Nigeria', 214028302],
    ['Brazil', 21171597],
    ['Russia', 141722205],
    ['Mexico', 128649565]
]

populated = filter(lambda c: c[1] > 300000000, countries)

print(list(populated))
```

## Utilisation de reduce

La fonction reduce est généralement utilisée pour des aggrégats sur des valeurs. Pour utiliser cette fonction, il faudra l'importer de la librairie 'functools'.

```python
# Par exemple pour faire la somme d'une liste:
from functools import reduce

scores = [75, 65, 80, 95, 50]
total = reduce(lambda a, b: a + b, scores)
print(total)
```

## List comporehensions

Il est parfois utile de créer des copies de liste et éventuellement d'y appliquer une fonction de transformation. Il existe en Python une écriture simplifiée qui permet de répondre à ce besoin. Assez simple à comprendre, l'exemple suivant permet de prendre la liste numbers et de créer une nouvelle liste en mettant chacune des entrées au carré.

```python
numbers = [1, 2, 3, 4, 5]
squares = [number**2 for number in numbers]
print(squares)
# Note: serait équivalent à la méthode de map suviante:
squares = list(map(lambda number: number**2, numbers))
print(squares)
```

Dans cette écriture, on peut ajouter une condition pour pouvoir filtrer sur les éléments que l'on souhaite retourner:

```python
mountains = [
    ['Makalu', 8485],
    ['Lhotse', 8516],
    ['Kanchendzonga', 8586],
    ['K2', 8611],
    ['Everest', 8848]
]

highest_mountains = [m for m in mountains if m[1] > 8600]
print(highest_mountains)
```

# Python Tuples

Un tuple est un type de liste que l'on ne peut pas modifier.

```python
# Initier une liste de tuples.
rgb = ('red', 'green', 'blue')
print(rgb[0])
print(rgb[1])
print(rgb[2])
# Initier un tuple avec un seul élément
numbers = (3,)
print(type(numbers))
# Si on omet la virgule, on va créer simplement un nombre.
numbers = (3)
print(type(numbers))
```

# Python Dictionary

Un dictionaire en Python est une collection de clé-valeur.