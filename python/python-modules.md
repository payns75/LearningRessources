# Python Modules

## Rechecrche des modules

La recherche des modules se fait soit:
- Dans le répertoire courant ou s'exécute le programme.
- Dans la liste des répertoires qui sont définis par la variable d'environnement PYTHONPATH.
- Dans les répertoires d'installation qui sont configurés lorsque l'on installe Python.

Le petit programme suivant nous donne la liste dans laquelle les modules sont recherchés:
```python 
import sys

for path in sys.path:
    print(path)
```

Pour importer le module qui se trouve dans un sous répertoire du projet en cours, on peut ajouter le répertoire dynamiquement à la liste des modules.
```python 
sys.path.append('.\\test\\')
from pricing import get_net_price as calculate_net_price
```
> blockquote Dans VsCode, pour éviter d'avoir une erreur dans l'éditeur, on peut ajouter le chemin dans setting.json (se fait facilement en click droit sur le block pour le corriger.)

## Utiliser les modules

Si par exemple, on a un fichier "pricing.py" avec le code suivant:
```python 
def get_net_price(price, tax_rate, discount=0):
    discounted_price = price * (1 - discount) 
    net_price = discounted_price * (1 + tax_rate) 
    return net_price


def get_tax(price, tax_rate=0):
    return price * tax_rate
```

Pour importer le module, il suffit de faire
```python 
import pricing

net_price = pricing.get_net_price(
    price=100,
    tax_rate=0.01
)

print(net_price)
```
Pour importer le module avec un nouveau nom, il faut ajouter l'alias avec la directive 'as' comme par exemple:
```python 
import pricing as selling_price
```
Pour n'importer que certaines fonctions, il suffit d'utiliser la syntaxe suivante:
```python 
from pricing import get_net_price
```
Pour cette dernière, il est aussi possible d'ajouter un alias:
```python 
from pricing import get_net_price as calculate_net_price
```
Pour importer directement toutes les fonctions, on peut utiliser la syntaxe:
```python 
from module_name import *
```
Attention, cette pratique n'est pas terrible car on pourrait sans le vouloir, overider une fonction ou une variable existante.

## Variable \_\_name\_\_

Cette variable nous permet de déterminer si on appel un module ou si on exécute direcement un module.

Si \_\_name\_\_ = "\_\_main\_\_", alors le module a été lancé directement. Si \_\_name\_\_ est égale au nom du module, alors il s'agit d'un import.

Généralement, on va tester cette variable \_\_name\_\_ lorsque l'on souhaite par exemple avoir un certain comportement:
- Si \_\_name\_\_ = "\_\_main\_\_" on va vouloir par exemple monter une exception du type "vous ne pouvez pas exécuter ce module directement" ou exécuter n'importe quel méthode
- Si \_\_name\_\_ != "\_\_main\_\_", on pourrait vouloir dire que "Ce module ne peut pas être référencé par une autre applciation".

## Gestion des packages

Pour faciliter la gestion des différents modules, il est possible d'organiser les fichiers par répertoire. Pour se faire, il suffit d'ajouter le fichier '__init__.py'. À partir de la version 3.3, il n'est plus nécessaire d'ajouter ce fichier.

Pour importer le package, il suffit de préfixer celui-ci avec le nom du répertoire.
```python 
import test.pricing
net_price = test.pricing.get_net_price(
    ...
```
ou (le as est optionnel)
```python 
from test.pricing import get_net_price as create_order
net_price = create_order(
    ...
```

Par convention, le code dans '__init__.py' permet d'initialiser le package. On pourrait par exemple y mettre des variables ou importer des modules automatiquement.
```python 
# import the order module automatically
from test.pricing import get_tax as tax
from test.subtest.plop import plop #si on avait un sour répertoire subtest

# default sales tax rate
TAX_RATE = 0.07
```
puis l'utiliser comme suit:
```python 
import test
print(test.TAX_RATE) #Affiche le taux
print(test.tax(100, test.TAX_RATE)) #Applique le taux
test.plop() #Appel le package d'un sous répertoire
```

## Fonctions privées

Pour rendre une fonction privée et donc non accessible aux autres packages, il suffit d'ajouter un '_' devant le nom de la fonction.
```python
def _attach_file(filename):
    print(f'Attach {filename} to the message')
```

Une autre façon de définir la visibilité des objets, est d'utiliser la variable \_\_all\_\_ pour n'y mettre que les objets accessibles depuis l'exterieur.

```python
__all__ = ['send']


def send(email, message):
    print(f'Sending "{message}" to {email}')


def attach_file(filename):
    print(f'Attach {filename} to the message')
```

De cette façon, seulement send sera accessible depuis l'extérieur.