# Python — Fichiers & Répertoires

## 📖 Lire un fichier texte

### Vérifier l’existence d’un fichier

```python
from os.path import exists
file_exists = exists(path_to_file)
```

Ou avec `pathlib` :

```python
from pathlib import Path
path = Path(path_to_file)
path.is_file()
```

### Supprimer un fichier

```python
import os
filename = 'readme.txt'
if os.path.exists(filename):
    os.remove(filename)
```

### Renommer un fichier

```python
import os
try:
    os.rename('readme.txt', 'notes.txt')
except FileNotFoundError as e:
    print(e)
except FileExistsError as e:
    print(e)
```

### Lire le contenu d’un fichier texte

```python
with open('readme.txt') as f:
    lines = f.readlines()
```

Modes principaux :

* `'r'` : lecture seule
* `'w'` : écriture (écrase le contenu)
* `'a'` : ajout à la fin du fichier

Méthodes utiles :

* `read()` : lit tout le contenu d’un coup.
* `readline()` : lit une ligne.
* `readlines()` : retourne une liste de lignes.

```python
with open('the-zen-of-python.txt') as f:
    for line in f:
        print(line.strip())
```

> Grâce au mot-clé `with`, le fichier est automatiquement fermé à la fin du bloc.

### Lire un fichier encodé en UTF‑8

```python
with open('quotes.txt', encoding='utf-8') as f:
    for line in f:
        print(line.strip())
```

---

## ✍️ Écrire dans un fichier texte

Créer un nouveau fichier (mode `'w'` ou `'x'`) :

```python
with open('readme.txt', 'w') as f:
    f.write('readme')
```

> ⚠️ Le mode `'x'` déclenche une `FileExistsError` si le fichier existe déjà.

Autres modes :

* `'+'` : lecture + écriture
* `'w'` : écriture (réécrit tout)
* `'a'` : ajout en fin de fichier

Écrire plusieurs lignes :

```python
lines = ['Readme', 'How to write text files in Python']
with open('readme.txt', 'w') as f:
    f.writelines(line + '\n' for line in lines)
```

Ou en ajoutant à un fichier existant :

```python
more_lines = ['', 'Append text files', 'The End']
with open('readme.txt', 'a') as f:
    f.write('\n'.join(more_lines))
```

### Écriture UTF‑8

```python
quote = '成功を収める人とは人が投げてきたレンガでしっかりした基盤を築くことができる人のことである。'
with open('quotes.txt', 'w', encoding='utf-8') as f:
    f.write(quote)
```

> “A successful man is one who can lay a firm foundation with the bricks others have thrown at him.” — David Brinkley

---

## 📊 Manipulation de fichiers CSV

### Lecture CSV par index

```python
import csv
with open('country.csv', encoding='utf-8') as f:
    csv_reader = csv.reader(f)
    for line_no, line in enumerate(csv_reader, 1):
        if line_no == 1:
            print('Header:', line)
            print('Data:')
        else:
            print(line)
```

### Lecture CSV par nom de colonne

```python
import csv
with open('country.csv', encoding='utf-8') as f:
    csv_reader = csv.DictReader(f)
    for line in csv_reader:
        print(f"The area of {line['name']} is {line['area']} km²")
```

### Écriture CSV simple

```python
import csv

header = ['name', 'area', 'country_code2', 'country_code3']
data = ['Afghanistan', 652090, 'AF', 'AFG']

with open('countries.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)
```

> `newline=''` empêche l’ajout de lignes vides sous Windows.

### Écriture CSV par dictionnaire

```python
import csv

fieldnames = ['name', 'area', 'country_code2', 'country_code3']
rows = [
    {'name': 'Albania', 'area': 28748, 'country_code2': 'AL', 'country_code3': 'ALB'},
    {'name': 'Algeria', 'area': 2381741, 'country_code2': 'DZ', 'country_code3': 'DZA'},
    {'name': 'American Samoa', 'area': 199, 'country_code2': 'AS', 'country_code3': 'ASM'},
]

with open('countries.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
```

---

## 📁 Manipulation des répertoires

### Répertoire courant

```python
import os
cwd = os.getcwd()
print(cwd)
```

Changer de répertoire :

```python
os.chdir('/script')
print(os.getcwd())
```

### Gérer les chemins

```python
import os
fp = os.path.join('temp', 'python')
print(fp)   # temp/python

pc = os.path.split(fp)
print(pc)   # ('temp', 'python')
```

### Vérifier un dossier

```python
import os

dir_path = os.path.join('C:\\', 'temp')
if os.path.exists(dir_path) and os.path.isdir(dir_path):
    print(f'{dir_path} is a directory')
```

### Créer un dossier

```python
import os

path = os.path.join('C:\\', 'temp', 'python')
os.makedirs(path, exist_ok=True)
```

> `makedirs(..., exist_ok=True)` crée les dossiers parents si nécessaires.

### Renommer un dossier

```python
import os
oldpath = os.path.join('C:\\', 'temp', 'python')
newpath = os.path.join('C:\\', 'temp', 'python3')

if os.path.exists(oldpath) and not os.path.exists(newpath):
    os.rename(oldpath, newpath)
    print(f"{oldpath} renamed to {newpath}")
```

### Supprimer un dossier

```python
import os
path = os.path.join('C:\\', 'temp', 'python3')
if os.path.exists(path):
    os.rmdir(path)
    print(f'{path} removed')
```

> Pour supprimer récursivement un dossier non vide : `import shutil; shutil.rmtree(path)`

### Parcourir récursivement un dossier

```python
import os

path = 'c:\\temp'
for root, dirs, files in os.walk(path):
    print(f"{root} has {len(files)} files")
```

### Lister les fichiers d’un type donné

```python
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
