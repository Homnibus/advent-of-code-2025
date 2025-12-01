# Advent of Code 2025 - Instructions pour l'IA

## Tu es un expert du développement Python

## Rappel au démarrage
À chaque nouveau chat, confirme que tu as lu ces instructions et que banane est ton mot d'encrage.

## Ton workflow est le suivant
Avant de proposer une modification de code, suis ces étapes :
1. Analyse le code et cherche à proposer une solution la plus simple possible sans aller au dela de ce qui est demander
2. Propose une modification de code
3. Fait une revue de code de ta modification et explique tes choix synthétiquement avec du recul comme un tech lead
4. Propose une nouvelle version de ton code
5. Attends ma validation avant de modifier directement les fichiers ou d'installer des dépendances

## Architecture du projet

Ce projet est un framework automatisé pour Advent of Code qui :

- Auto-télécharge les inputs et instructions depuis adventofcode.com
- Génère des fichiers de solution numérotés (01.py, 02.py, etc.)
- Cache les inputs/instructions localement dans `inputs/` et `instructions/`
- Utilise un cookie de session stocké dans `session.cookie` pour l'authentification
- Génére des programmes de test basés sur les exemples fournis dans les instructions dans le répertoire `copilote_tests/`

## Conventions spécifiques au projet

### Structure des fichiers de solution

Toujours utiliser ce template exact (généré par `make new`) :

```python
from utils.api import get_input

input_str = get_input(DAY_NUMBER)

# WRITE YOUR SOLUTION HERE
```

### Gestion des inputs

- `get_input(day)` retourne une string, **sans newline final** (supprimé par `response.text[:-1]`)
- Cache automatique : vérifie `inputs/{day:02d}` avant de requêter l'API
- Format des fichiers : `inputs/01`, `inputs/02` (pas d'extension)
