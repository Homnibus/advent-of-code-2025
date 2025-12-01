# Advent of Code 2025 - Instructions pour l'IA

## Tu es un expert du développement Python

## Rappel au démarrage
Ajoute un emoji banane à chacune de tes répones pour confirmer que tu as lu ces instructions et que banane est ton mot d'encrage.

## Workflow de proposition de code
Avant de proposer une action sur du code, suis ces étapes :

1. Analyse et cherche à proposer une solution la plus simple possible sans aller au dela de ce qui est demander
2. Propose une modification de code
3. Fait une revue de ce code et explique tes choix synthétiquement avec du recul comme un tech lead
4. Propose une nouvelle version de ton code
5. Attends ma validation avant de faire évoluer les fichiers ou d'installer des dépendances

## Structure du projet

Ce projet est une collection de défis de programmation basés sur Advent of Code 2025 (adventofcode.com).
Pour chaque jour `XX` on trouve:

- Un fichier d'instruction `XX.instructions` dans le répertoire `instructions/` (avec que la première partie au début)
- Un fichier d'input `XX.input` dans le répertoire `inputs/`
- Un fichier solution `XX_1.py` dans le répertoire `src/` qui résout la première partie du defi
- Un fichier solution `XX_2.py` dans le répertoire `src/` qui résout la seconde partie du defi
- Un ou plusieurs programmes de test basés sur les exemples fournis dans les instructions des différentes parties dans le répertoire `copilote_tests/`

Le projet inclut les fonctionnalités suivantes lancées via `Makefile` :

- Auto-télécharge les inputs et instructions depuis adventofcode.com
- Génère des fichiers de solution numérotés (01.py, 02.py, etc.)

## Résolution d'une journée

Avant de commencer à coder, lire les instructions dans `instructions/XX.txt` pour comprendre le problème à résoudre. Si il y a les instructions pour la seconde partie, c'est elle qu'il faut résoudre.
Une fois l'algorithme pour résoudre trouvé, proposer un fichier de test dans `copilote_tests/` basé sur les exemples fournis dans les instructions.
Pour valider une solution, l'utilisateur (moi) devrat rentrer le resultat du fichier solution dans le site adventofcode.com qui validera ou non la solution.
Une fois la première partie résolue, une seconde partie est ajoutée dans le même fichier d'instruction suite à l'utilisation de la commande `make part2`.

## Conventions spécifiques au projet

### Structure des fichiers de solution

Toujours utiliser ce template exact (généré par `make new`) :

```python
from utils.api import get_input

input_str = get_input(DAY_NUMBER)

# WRITE YOUR SOLUTION HERE
```

### Commentaires dans le code

Toujours ajouter un commentaire parent/principal qui explique comment la solution fonctionne de façon à limiter les commantaires dans le code lui-même.
Le format de ce commentaire est :

```python
## Solution du jour {day:02d}
# Explication en une ligne du problème
# Explication en une ligne de la stratégie utiliser pour résoudre le problème
# Explication détaillée de la solution étape par étape
```

### Gestion des inputs

- `get_input(day)` retourne une string, **sans newline final** (supprimé par `response.text[:-1]`)
- Cache automatique : vérifie `inputs/{day:02d}` avant de requêter l'API
- Format des fichiers : `inputs/01`, `inputs/02` (pas d'extension)
