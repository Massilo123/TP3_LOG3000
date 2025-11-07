# Module `tests`

## Objectif
Valider automatiquement les règles métiers de la calculatrice Flask et détecter les régressions. Les tests actuels ciblent les opérations arithmétiques de base et les scénarios d'erreur simples.

## Contenu principal
- `test_calculator.py` : cas de test `pytest` qui exercent la fonction `calculate` exposée par `app.py`. Chaque test possède un docstring décrivant le comportement attendu.

## Exécution
1. Installer les dépendances nécessaires (depuis la racine du projet) :
   ```powershell
   pip install pytest
   ```
2. Lancer toute la suite :
   ```powershell
   pytest
   ```


