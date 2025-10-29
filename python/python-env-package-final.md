# 🐍 Python — PIP, Packages tiers & Environnements virtuels

> Référence pratique pour gérer les dépendances Python, les environnements isolés et les certificats d’entreprise (ex. ZScaler).

---

## 📦 Gestion des packages avec PIP

### 🔎 Vérifier la version de PIP

```powershell
# Sous Windows
pip --version
# Sous Linux ou macOS
pip3 --version
```

### 📥 Installer un package

```powershell
pip install requests
```

Exemple d’utilisation :

```python
import requests
response = requests.get('https://pypi.org/')
print(response.status_code)
```

### 🧩 Installer une version spécifique

```powershell
pip install requests==2.20.1
```

### 📋 Lister les packages installés

```powershell
pip list
```

### 🕐 Lister les packages obsolètes

```powershell
pip list --outdated
```

### 🗑️ Désinstaller un package

```powershell
pip uninstall <nom_du_package>
```

### 🔍 Voir les dépendances et informations d’un package

```powershell
pip show requests
```

---

## 🔐 Installation derrière un proxy ZScaler (ou équivalent)

Lorsque l’accès HTTPS est intercepté, `pip` peut échouer à vérifier les certificats SSL.

### Étapes pour configurer le certificat racine :

1. Aller sur un site HTTPS (ex. `https://pypi.org`).

2. Cliquer sur le **cadenas** dans le navigateur → exporter le **certificat racine** au format **Base‑64 (.CER)**.

3. Copier ce fichier vers un répertoire local, par ex. :

   ```
   C:\dev\certs\ZscalerRootCA.pem
   ```

4. Trouver le chemin du fichier de configuration `pip.ini` :

   ```powershell
   python -m pip config debug
   ```

   Exemple de résultat : `C:\Users\<user>\AppData\Local\Programs\Python\Python313\pip.ini`

5. Créer/éditer ce fichier et ajouter :

   ```ini
   [global]
   cert = C:\dev\certs\ZscalerRootCA.pem
   ```

6. Redémarrer le terminal PowerShell / VSCode.

> 💡 Cette configuration permet à `pip` de valider les certificats SSL internes (corporate proxy).

---

## 🧱 Environnements virtuels (venv)

> Objectif : isoler les dépendances de chaque projet Python.

### 🪄 Créer un environnement virtuel

```powershell
python -m venv .venv
```

Cela crée un dossier `.venv/` contenant un interpréteur Python isolé et ses dépendances.

### ▶️ Activer l’environnement

```powershell
.venv\Scripts\activate
```

> Après activation, la ligne de commande affiche le préfixe `(.venv)`.

Vérifie que Python pointe bien vers l’environnement :

```powershell
Get-Command python
```

> Le chemin doit contenir `.venv`.

### ⏹️ Désactiver l’environnement

```powershell
deactivate
```

---

## 📑 Fichier `requirements.txt`

Exporter la liste des dépendances installées :

```powershell
pip freeze > requirements.txt
```

Installer toutes les dépendances d’un projet sur un autre poste :

```powershell
pip install -r requirements.txt
```

> 💡 Toujours régénérer ce fichier avant un commit important ou un déploiement.

---

## 🧠 Intégration VS Code

Pour que VS Code détecte l’environnement virtuel :

1. Ouvre la **palette de commandes** (`Ctrl + Shift + P`).
2. Recherche : `Python: Select Interpreter`.
3. Sélectionne l’interpréteur situé dans ton dossier `.venv`.

Cela garantit :

* une **analyse correcte** du code (Pylance),
* un **débogage** dans le bon environnement.

---

## 📜 Note sur les certificats et `requests`

Si ton environnement virtuel ne contient pas le certificat ZScaler, certaines requêtes HTTPS échoueront.

### 🚫 Mauvaise pratique (à éviter sauf test)

```python
import requests
response = requests.get('https://www.google.com', verify=False)
if response.status_code == 200:
    print(response.text)
```

> ⚠️ `verify=False` désactive toute vérification SSL — dangereux en production.

### ✅ Bonne pratique

Installe le certificat racine dans l’environnement ou fais pointer `verify` vers ton fichier PEM :

```python
response = requests.get('https://www.google.com', verify='C:/dev/certs/ZscalerRootCA.pem')
```

---

## ✅ Résumé des bonnes pratiques

* Utilise toujours un **environnement virtuel par projet** (`python -m venv .venv`).
* **Versionne** ton `requirements.txt`, pas le dossier `.venv`.
* **Vérifie les certificats** internes si tu es derrière un proxy HTTPS.
* **Évite** `verify=False` sauf pour du debug local.
* **Garde PIP à jour** :

  ```powershell
  python -m pip install --upgrade pip
  ```
