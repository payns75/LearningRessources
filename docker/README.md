# Installation

Pour faire fonction ce mini projet d'IA, les lignes de commandes suivantes doivent être exécutées dans le répertoire 'docker'.

Dans le répertoire 'docker', s'assurer que le répertoire 'models' existe.

## Démarrer le service

```bash
cd .\mistral-local
docker compose build --no-cache
docker compose up -d
```

## Installation de Mistral le plus léger

```bash
docker exec -it ollama ollama pull mistral:7b-instruct-q2_K
```

## Exécuter le modèle

```bash
docker exec -it ollama ollama run mistral:7b-instruct-q2_K
```