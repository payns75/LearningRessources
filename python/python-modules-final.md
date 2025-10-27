# Python — Modules & Packages

## 🔎 Où Python cherche les modules ?

Python cherche les modules dans cet ordre :

1. Le **répertoire courant** d’exécution du programme.
2. Les répertoires listés dans la variable d’environnement **`PYTHONPATH`**.
3. Les répertoires d’**installation** de Python (ex. `site-packages`).

Lister l’ordre effectif :

```python
import sys
for path in sys.path:
    print(path)
```

**Astuce VS Code**
Pour que l’éditeur (pylance) trouve les modules locaux sans bidouiller le code, ajouter des chemins dans `.vscode/settings.json` :

```json
{
  "python.analysis.extraPaths": ["./test", "./src"]
}
```

> Évite de modifier `PYTHONPATH` globalement. Privilégie un venv + une structure de package propre.

---

## 🔗 Importer un module/fonction

Supposons un fichier `pricing.py` :

```python
def get_net_price(price, tax_rate, discount=0):
    discounted_price = price * (1 - discount)
    net_price = discounted_price * (1 + tax_rate)
    return net_price

def get_tax(price, tax_rate=0):
    return price * tax_rate
```

Importer le module :

```python
import pricing
net_price = pricing.get_net_price(price=100, tax_rate=0.01)
print(net_price)
```

Lui donner un alias :

```python
import pricing as selling_price
```

Importer une fonction précise :

```python
from pricing import get_net_price
```

Avec alias :

```python
from pricing import get_net_price as calculate_net_price
```

Importer *tout* (déconseillé) :

```python
from pricing import *  # ❌ Risque d’écraser des noms
```

---

## ➕ Ajouter temporairement un chemin d’import (à éviter en prod)

Si tu veux importer un module situé dans un sous-dossier **pour un script ponctuel** :

```python
import sys
from pathlib import Path

# Ajoute le dossier "test" à sys.path en tête, de façon portable
sys.path.insert(0, str(Path(__file__).parent / "test"))
from pricing import get_net_price as calculate_net_price
```

> Préfère une vraie structure de package + `pip install -e .` pour les projets.

---

## 🔁 `__name__` et le point d’entrée

`__name__` vaut :

* `"__main__"` quand le fichier est **exécuté directement**,
* le **nom du module** quand il est **importé**.

Patron classique :

```python
def main():
    # logique de test/CLI
    ...

if __name__ == "__main__":
    main()
```

> Évite de lever des exceptions « si exécuté directement » sauf cas particulier. Ce bloc sert surtout aux tests rapides/CLI.

---

## 📦 Packages (répertoires de modules)

* Un **package** est un répertoire contenant des modules ; `__init__.py` est **optionnel depuis Python 3.3** (namespace packages), mais souvent on le garde pour **initialiser** / **ré-exporter** proprement.

Importer un sous-module :

```python
import test.pricing
net_price = test.pricing.get_net_price(...)
```

Ou importer une fonction avec alias :

```python
from test.pricing import get_net_price as create_order
net_price = create_order(...)
```

`__init__.py` (initialisation / ré-exports) :

```python
# test/__init__.py
from .pricing import get_tax as tax  # import relatif
# from .subtest.plop import plop

TAX_RATE = 0.07
```

Utilisation :

```python
import test
print(test.TAX_RATE)
print(test.tax(100, test.TAX_RATE))
# test.plop()
```

> **Bonnes pratiques d’import dans un package** : utilise des **imports relatifs** (`from .pricing import ...`) à l’intérieur du package.

---

## 🔒 Visibilité : privé / public

* Un nom préfixé par **`_`** (underscore) est **privé par convention** (pas d’interdiction technique).
* La variable **`__all__`** contrôle **ce que `from module import *` importe**. Elle **n’empêche pas** d’accéder à d’autres noms via `module.nom`.

Exemples :

```python
# Convention « privé »
def _attach_file(filename):
    print(f"Attach {filename} to the message")

# Contrôler les imports étoilés
__all__ = ["send"]

def send(email, message):
    print(f'Sending "{message}" to {email}')

def attach_file(filename):
    print(f'Attach {filename} to the message')
```
