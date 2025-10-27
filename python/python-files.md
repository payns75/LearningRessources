# Manipulation de fichiers ou de répertoires

## Lire un fichier texte

Pour vérifier si un fichier existe ou non, on peut uiliser:
```Python
from os.path import exists
file_exists = exists(path_to_file)
```

ou

```Python
from pathlib import Path
path = Path(path_to_file)
path.is_file()
```

Pour supprimer un fichier:
```Python
import os
filename = 'readme.txt'
if os.path.exists(filename):
    os.remove(filename)
```

Pour renomer un fichier:
```Python
import os
try:
    os.rename('readme.txt', 'notes.txt')
except FileNotFoundError as e:
    print(e)
except FileExistsError as e:
    print(e)
```

Pour lire simplement un fichier texte en python, il suffit de mettre en place le code suivant:

```Python
with open('readme.txt') as f:
    lines = f.readlines()
```

- On ouvre le fichier avec open(path, mode) avec mode:
    - 'r': Lecture seule
    - 'w': Écriture
    - 'a': Ajouter du texte
- On va lire le fichier, soit avec:
    -  read(): va lire tout le fichier
    - readline(): va lire le fichier ligne par ligne
    - readlines(): va lire tout le fichier et mettre le résultat dans un tableau ligne par ligne. A utiliser avec strip() pour nettoyer les lignes vide (\n)
- On cloture le fichier. Avec l'opérateur 'with', le fichier est clôturé automatiquement.

```Python
with open('the-zen-of-python.txt') as f:
    for line in f:
        print(line.strip())
```

## Lire un fichier text UTF-8
```Python
with open('quotes.txt', encoding='utf8') as f:
    for line in f:
        print(line.strip())
```

## Écrire dans un fichier texte
Pour créer un nouveau fichier, il faut l'ouvrir avec le mode 'w' ou 'x'.
> Avec le mode x, si le fichier existe déjà, il y aura une exception FileExistsError.

```Python
with open('readme.txt', 'w') as f:
    f.write('readme')
```

- On ouvre le fichier avec open(path, mode) avec mode:
    - '+': Ouvrir le fichier pour à la fois écrire et lire
    - 'w': Écriture, remplace le contenu.
    - 'a': Ajouter du texte au contenu existant.
- On va écrire dans le fichier avec l'une des méthodes suivantes:
    - write(): Écrit un bloque de texte complet dans le fichier.
    - writelines(): Écrit dans le fichier ligne par ligne.
On cloture le fichier. Avec l'opérateur 'with', le fichier est clôturé automatiquement.

```Python
lines = ['Readme', 'How to write text files in Python']
with open('readme.txt', 'w') as f:
    f.writelines(lines)
```
ou
```Python
more_lines = ['', 'Append text files', 'The End']
with open('readme.txt', 'a') as f:
    f.write('\n'.join(more_lines))
```

## Écrire un fichier UTF-8

```Python
quote = '成功を収める人とは人が投げてきたレンガでしっかりした基盤を築くことができる人のことである。'
with open('quotes.txt', 'w', encoding='utf-8') as f:
    f.write(quote)
```
> A successful man is one who can lay a firm foundation with the bricks others have thrown at him. – David Brinkley

## Manipulation d'un fichier CSV

### Lecture d'un fichier CSV et accès par index

Ce exemple illustre comment lire un fichier csv et décompose le header. On accède ensuite aux éléments via line[0], line[1].

```Python
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
```

### Lecture d'un fichier CSV et accès par nom de colonne

```Python
import csv
with open('country.csv', encoding="utf8") as f:
    csv_reader = csv.DictReader(f)
    # skip the header
    next(csv_reader)
    # show the data
    for line in csv_reader:
        print(f"The area of {line['name']} is {line['area']} km2")
```

### Écriture dans un fichier CSV

L'exemple suivant démontre comment écrire dans un fichier CSV UTF-8

```Python
import csv  

header = ['name', 'area', 'country_code2', 'country_code3']
data = ['Afghanistan', 652090, 'AF', 'AFG']

with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    writer.writerow(data)
```

> newline='' supprime les lignes vides à l'ouverture du fichier.

Ou, une autre façon de modifier un fichier CSV, en passant par les noms de colonnes du fichier + ajouter plusieurs lignes.

```Python
import csv

# csv header
fieldnames = ['name', 'area', 'country_code2', 'country_code3']

# csv data
rows = [
    {'name': 'Albania',
    'area': 28748,
    'country_code2': 'AL',
    'country_code3': 'ALB'},
    {'name': 'Algeria',
    'area': 2381741,
    'country_code2': 'DZ',
    'country_code3': 'DZA'},
    {'name': 'American Samoa',
    'area': 199,
    'country_code2': 'AS',
    'country_code3': 'ASM'}
]

with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
```

## Manipulation des répertoires

### Répertoire de travail courant

```Python
import os
cwd = os.getcwd()
print(cwd)
```

Pour changer le répertoire de travail courant

```Python
import os
os.chdir('/script')
cwd = os.getcwd()
print(cwd)
```

### Manipulation sur les chemins de fichiers

```Python
import os

fp = os.path.join('temp', 'python')
print(fp)  # temp\python (on Windows)

pc = os.path.split(fp)
print(pc)  # ('temp', 'python')
```

### Test if a path is a directory

```Python
import os

dir = os.path.join("C:\\", "temp")
print(dir)

if os.path.exists(dir) or os.path.isdir(dir):
    print(f'The {dir} is a directory')
```

### Create a directory

```Python
import os

dir = os.path.join("C:\\", "temp", "python")
if not os.path.exists(dir):
    os.mkdir(dir)
```

### Rename a directory

```Python
import os

oldpath = os.path.join("C:\\", "temp", "python")
newpath = os.path.join("C:\\", "temp", "python3")

if os.path.exists(oldpath) and not os.path.exists(newpath):
    os.rename(oldpath, newpath)
    print("'{0}' was renamed to '{1}'".format(oldpath, newpath))
```

### Delete a directory

```Python
import os

dir = os.path.join("C:\\","temp","python")
if os.path.exists(dir):
    os.rmdir(dir)
    print(dir + ' is removed.')
```

### Traverse a directory recursively 

```Python
import os

path = "c:\\temp"
for root, dirs, files in os.walk(path):
    print("{0} has {1} files".format(root, len(files)))
```

### Rechercher la liste des fichiers dans un répertoire

```Python
import os
path = 'D:\\web'

html_files = []

for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        if filename.endswith('.html'):
            html_files.append(os.path.join(dirpath, filename))

for html_file in html_files:
    print(html_file)
```