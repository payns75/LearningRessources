# 🐳 Docker Cheat Sheet — AI-Analyze Stack

> Résumé complet des commandes Docker, des modèles Dockerfile et des bonnes pratiques pour le stack **RAG / AI-Analyze** sous Windows (WSL2 / Hyper-V).

---

## 🧩 1. Core Docker CLI

### 🔹 Versions, info et contextes

```bash
docker --version
docker info
docker context ls
docker context use default
```

### 🔹 Images

```bash
docker images
docker pull <image>[:tag]
docker rmi <image_id_or_repo:tag>
docker image inspect <image>
docker history <image>
```

### 🔹 Conteneurs

```bash
docker ps              # conteneurs actifs
docker ps -a           # tous les conteneurs
docker run --name myapp -p 8080:8080 -d <image>:tag
docker stop <container>
docker start <container>
docker restart <container>
docker rm <container>
docker inspect <container>
```

### 🔹 Exécution, copie, logs

```bash
docker exec -it <container> sh
docker cp <container>:/path/in/container C:\dest
docker cp C:\src\file.txt <container>:/tmp/
docker logs <container>
docker logs -f <container>    # suivi temps réel
```

### 🔹 Réseaux et volumes

```bash
docker network ls
docker network inspect <net>
docker network create mynet
docker network connect mynet <container>

docker volume ls
docker volume inspect <vol>
docker volume prune
```

### 🔹 Nettoyage système

```bash
docker system df
docker system prune
docker system prune -a     # supprime les images non utilisées
```

---

## 🧱 2. Docker Compose

### 🔹 Cycle de vie

```bash
docker compose up -d --build
docker compose build --no-cache
docker compose ps
docker compose logs -f
docker compose stop
docker compose down
docker compose down -v     # supprime aussi les volumes nommés
```

### 🔹 Commandes par service

```bash
docker compose exec <service> sh
docker compose logs -f <service>
```

### 🔹 Exemple de Healthcheck

```yaml
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost:8000/healthz"]
  interval: 10s
  timeout: 3s
  retries: 5
  start_period: 10s
```

---

## 🤖 3. Commands for the RAG Stack

### 🔹 Ollama

```bash
docker exec -it <ollama> ollama list
docker exec -it <ollama> ollama pull mistral:7b-instruct
docker exec -it <ollama> ollama pull qwen2.5-coder:7b
docker exec -it <ollama> ollama pull nomic-embed-text
docker exec -it <ollama> ollama embeddings -m nomic-embed-text "hello world"
```

**Vérification HTTP :**

```bash
curl -I http://localhost:11434
curl http://localhost:11434/api/tags
```

### 🔹 Qdrant

```powershell
Invoke-RestMethod -Uri "http://localhost:6333/collections"
Invoke-RestMethod -Uri "http://localhost:6333/collections/local_corpus/points/count" `
  -Method POST -Body '{}' -ContentType "application/json"
Invoke-RestMethod -Uri "http://localhost:6333/collections/local_corpus/points/scroll" `
  -Method POST -Body '{"limit":5,"with_payload":true,"with_vector":false}' `
  -ContentType "application/json" | ConvertTo-Json -Depth 5
```

### 🔹 FastAPI (ragapi)

```bash
curl http://localhost:8000/healthz
start http://localhost:8000/docs
```

---

## ⚙️ 4. Dockerfile Patterns

### 🧰 Multi-stage Build (recommandé)

#### Python (FastAPI)

```dockerfile
FROM python:3.11-slim AS build
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && pip wheel --no-cache-dir --wheel-dir=/wheels -r requirements.txt

FROM python:3.11-slim
WORKDIR /app
COPY --from=build /wheels /wheels
RUN pip install --no-cache /wheels/*
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

#### Node.js

```dockerfile
FROM node:20-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:20-alpine
WORKDIR /app
ENV NODE_ENV=production
COPY --from=build /app/dist ./dist
COPY package*.json ./
RUN npm ci --omit=dev
EXPOSE 3000
CMD ["node", "dist/server.js"]
```

#### .NET

```dockerfile
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src
COPY *.sln .
COPY src/ ./src/
RUN dotnet restore
RUN dotnet publish -c Release -o /out

FROM mcr.microsoft.com/dotnet/aspnet:8.0
WORKDIR /app
COPY --from=build /out .
EXPOSE 8080
ENTRYPOINT ["dotnet", "MyApp.dll"]
```

### ⚡ Single-Stage (POC rapide)

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

### 🔹 GPU workloads

```dockerfile
FROM nvidia/cuda:12.4.1-runtime-ubuntu22.04
# requires NVIDIA Container Toolkit and --gpus=all
```

### 🔹 Sécurité & hygiène

```dockerfile
RUN adduser -u 10001 -D appuser
USER appuser
```

> Toujours inclure un `.dockerignore` pour exclure `node_modules`, `.git`, `__pycache__`, etc.

---

## 🔧 5. Troubleshooting Patterns

### 🔹 Réseau interne

```bash
docker exec -it <container> sh
curl -I http://qdrant:6333/collections
curl -I http://ollama:11434
```

### 🔹 Proxy / SSL corporatif

```yaml
environment:
  HTTP_PROXY: http://proxy.xxx.qc.ca:8080
  HTTPS_PROXY: http://proxy.xxx.qc.ca:8080
  NO_PROXY: localhost,127.0.0.1,qdrant,ollama
```

### 🔹 Encodage (PowerShell)

```powershell
$payload = @{ query="..."; k=4 } | ConvertTo-Json
$bytes = [Text.Encoding]::UTF8.GetBytes($payload)
Invoke-RestMethod -Method POST -Uri http://localhost:8000/query -Body $bytes -ContentType "application/json; charset=utf-8"
```

### 🔹 Séquencement de démarrage

```python
# in app.py
for i in range(10):
    try:
        requests.get(f"{QDRANT_URL}/collections")
        break
    except:
        time.sleep(2)
```

> `depends_on` ne garantit pas la disponibilité — ajouter un healthcheck ou un “wait loop”.

---

## 💾 6. Gestion de la VM Docker (WSL2 / Hyper-V)

### 🔹 Inspection et contrôle

```bash
wsl --status
wsl --list --verbose
wsl --shutdown
wsl --terminate <DistroName>
```

### 🔹 Limiter les ressources (`%UserProfile%\\.wslconfig`)

```ini
[wsl2]
memory=8GB
processors=4
swap=8GB
localhostForwarding=true
```

**Appliquer :**

```bash
wsl --shutdown
# puis redémarrer Docker Desktop
```

### 🔹 Export / import de snapshots

```bash
wsl --export <DistroName> C:\\backup\\mydistro.tar
wsl --import <NewName> C:\\WSL\\NewPath C:\\backup\\mydistro.tar --version 2
```

### 🔹 Réinitialiser Docker Desktop

```bash
docker system prune -a
docker volume prune
```

---

## 🧠 7. RAG Stack — Quick Reference

### 🔹 Exemple de docker-compose simplifié

```yaml
services:
  ollama:
    image: ollama/ollama:latest
    ports: ["11434:11434"]
    volumes: ["ollama:/root/.ollama"]

  qdrant:
    image: qdrant/qdrant:latest
    ports: ["6333:6333"]
    volumes: ["qdrant_storage:/qdrant/storage"]

  ragapi:
    build: ./rag-api
    depends_on: [ollama, qdrant]
    environment:
      OLLAMA_BASE_URL: http://ollama:11434
      QDRANT_URL: http://qdrant:6333
      QDRANT_COLLECTION: local_corpus
      RAG_EMBED_MODEL: nomic-embed-text
      RAG_CHAT_MODEL: qwen2.5-coder:7b
    volumes: ["./data:/app/data:rw"]
    ports: ["8000:8000"]

volumes:
  ollama:
  qdrant_storage:
```

### 🔹 Sanity checks

```bash
# Ollama
docker exec -it ai-analyze-ollama-1 ollama list

# Qdrant
Invoke-RestMethod -Uri "http://localhost:6333/collections"

# RAG API
curl http://localhost:8000/healthz

# Ré-ingestion & vérification
.\ps\rag-ingest.ps1
Invoke-RestMethod -Uri "http://localhost:6333/collections/local_corpus/points/count" `
  -Method POST -Body '{}' -ContentType "application/json"
```

---

## 🧩 8. Dockerfile Reference Table

| Objectif           | Base Image                                      | Notes                                  |
| ------------------ | ----------------------------------------------- | -------------------------------------- |
| Minimal Python API | `python:3.11-slim`                              | Utiliser multi-stage + wheels          |
| Node API           | `node:20-alpine`                                | Multi-stage, omettre deps dev          |
| .NET API           | `mcr.microsoft.com/dotnet/sdk:8.0 → aspnet:8.0` | `dotnet publish` recommandé            |
| GPU workloads      | `nvidia/cuda:runtime`                           | Nécessite `--gpus=all`                 |
| Fast builds        | any                                             | Utiliser `.dockerignore` et cache deps |
| Secure build       | any                                             | Utilisateur non root + image minimale  |
