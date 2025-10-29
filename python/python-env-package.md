# Third-party Packages, PIP, and Virtual Environments

## Python pip

### Versions

```ps
# Sous Windows
pip --version
# Sous Linux ou mac
pip3 --version
```

### Pour installer un package, ici par exemple le package 'requests'

```ps
pip install requests
```

On peut maintenant utiliser la librairie comme par exemple:

```python
import requests
response = requests.get('https://pypi.org/')
print(response.status_code)
```

### Pour installer une version spécifique, ic la 2.20.1

```ps
pip install requests==2.20.1
```

### Pour lister les packages installés

```ps
pip list
```

### Pour la liste des packages périmés

```ps
pip list --outdated
```


### Désinstaller un package

```ps
pip uninstall <package_name>
```

### Afficher les dépendances d'un package

```ps
pip show requests
```

### Aide de l'installation derrière ZScaler

- Récupérer le certificat en allant sur un site https par exemple 'https://pypi.org'
- Cliquer dans chrome ou edge sur le cadenat pour récupérer le certificat et exporter la racine en Base-64 (.CER)
- Déplacer le certificat dans un répertoire sur le poste, par exemple 'C:\dev\certs\ZscalerRootCA.pem'
- Aller voir ou se trouvent les fichier de configuration 'pip.ini' en tapant la config suivante:
```ps
python -m pip config debug
````
- Prendre le chemin vers le site, par exemple 'C:\Users\a91\AppData\Local\Programs\Python\Python313\pip.ini', le créer le cas échéant.
- Faire pointer la variable de certificat vers le répertoire local, par exemple:
```ps
[global]
cert = C:\dev\certs\ZscalerRootCA.pem
````
- Redémarrer la console si nécessaire

## Python Virtual Environments

Afin d'isoler un environnement de développement et pour pleins d'autres bonnes raisons ;), il est fortement conseillé de créer un environnement virtuel lorsque l'on travail sur un projet Python.

### Créer l'environnement

```ps
python -m venv .venv
```

Cela va créer un répertoire '.venv' avec tout ce qu'il faut pour exécuter notre projet Python.

### Activer l'environnement

```ps
.venv\Scripts\activate
```

En exécutant ce batch, on va activer et entrer dans l'environnement. La ligne de commande va être maintenant préfixée par '(.venv)'

Si l'on tape maintenant la commande power shell
```ps
get-command python
```
On va vérifier que le programme 'python.exe' aura un chemin qui va pointer vers le répertoire '.venv'.

### Sortir de l'environement virtuel

```ps
deactivate
```

### Requirement.txt

Après avoir installé différents packages pour le projet, il est nécessaire de créer un fichier de requis qui pourra être utilisé pour restaurer les packages sur d'autres machines.

```ps
pip freeze > requirements.txt
```

Il suffira alors, pour restaurer les packages sur un autre poste de le faire avec la ligne de commande suivante:

```ps
pip install -r requirements.txt
```

### Note pour VsCode

Il faut sélectionner l'environnement pour que VsCode fonctionne correctement, que ce soit pour l'analyse du code ou pour le débuggage.
- Ouvrir la palette de command avec CTRL+SHIFT+P
- Rechercher 'Python: Select Interpreter'
- Sélectionner l'environnement qui se trouve sous le répertoire .venv par exemple.

### Note pour les certificats

Dans la librairie 'requests' par exemple, il y a un problème de certificats lorsque l'on essaye d'accéder à des sites HTTPS.

Pour le moment je n'ai pas résolu le problème, un contournement temporaire est d'ajouter à 'verify' la valeur 'False' (alors qu'elle devrait pointer vers le certificat, mais cela ne fonctionne pas). Ou mieux, que le certificat soit installé dans l'environnement.

```Python
import requests
response = requests.get('https://www.google.com', verify=False)
if response.status_code == 200:
    print(response.text)
```