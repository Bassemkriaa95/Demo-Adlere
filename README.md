# Demo DevOps AI

Cette démonstration contient une petite API Flask située dans le dossier `devops-ai-demo`.

## Prérequis

- Python 3.12 ou Docker
- Git

## Exécuter l'application avec `run.sh`

Depuis la racine du dépôt :

```bash
cd devops-ai-demo
chmod +x run.sh
./run.sh
```

L'application sera disponible sur <http://localhost:5000>.

## Exécuter l'application avec Docker

Depuis la racine du dépôt :

```bash
cd devops-ai-demo
docker build -t devops-ai-demo .
docker run --rm -p 5000:5000 devops-ai-demo
```

Ouvrez ensuite <http://localhost:5000>.

## Erreurs à corriger pour le demo

1. Dans `app.py`, importer `jsonify` depuis Flask :

```python
from flask import Flask, jsonify
```

2. Dans `app.py`, faire écouter Flask sur toutes les interfaces réseau :

```python
app.run(host="0.0.0.0", port=5000)
```

3. Dans le `Dockerfile`, exposer le même port que l'application :

```dockerfile
EXPOSE 5000
```
