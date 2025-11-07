# Calculatrice web — TP3 LOG3000

## Numéro d’équipe
28

## Description du projet
Application web minimaliste, écrite avec Flask, qui expose une calculatrice arithmétique élémentaire. L’interface web permet de saisir une expression contenant deux opérandes et un seul opérateur (`+`, `-`, `*`, `/`). Le serveur valide la saisie, effectue l’opération en Python et renvoie le résultat ou un message d’erreur formaté. Le dépôt inclut également la structure HTML/CSS et une documentation de module pour guider les nouveaux contributeurs.

## Prérequis
- Python 3.10 ou plus
- `pip` 
- Accès internet pour installer les dépendances

## Installation pas à pas
1. **Cloner le dépôt**  
   `git clone <url-du-depot>`  
   `cd TP3_LOG3000`
2. **Installer les dépendances**  
   `pip install flask`

## Utilisation
1. Démarrer l’application : `python app.py`
2. Ouvrir un navigateur à l’adresse `http://127.0.0.1:5000`
3. Utiliser les boutons pour composer une expression : chiffres de `0` à `9`, opérateurs `+`, `-`, `*`, `/` et `C` pour effacer.
4. Cliquer sur `=` pour envoyer l’expression au serveur et afficher le résultat dans la zone de texte.
5. En cas d’expression invalide (plusieurs opérateurs, opérandes non numériques, etc.), un message d’erreur lisible est affiché.

## Tests
Les tests automatisés résident dans le dossier `tests/` (à créer si absent) et sont basés sur `pytest`.

1. Installer les dépendances de test :  
   `pip install pytest`
2. Lancer l'ensemble des tests :  
   `pytest`
3. Si un test échoue :
   - Noter le nom du test, le message d'erreur et les étapes de reproduction.
   - Créer une issue GitHub dédiée en assignant un membre de l'équipe et en décrivant le cas d'échec.
   - Ouvrir une branche spécifique pour le correctif, appliquer la correction, relancer `pytest`.
   - Pousser la branche et ouvrir une Pull Request qui mentionne l'issue correspondante.


## Flux de contribution
1. **Créer une issue** pour tout nouveau bug ou évolution en documentant clairement le besoin.
2. **Créer une branche dédiée** (`git checkout -b fix/<issue-id>` ou `feature/<description>`).
3. **Développer et tester** localement (relancer `pytest` et faire les validations manuelles nécessaires).
4. **Mettre à jour la documentation** (docstrings, README de module, README principal) si la modification impacte le fonctionnement.
5. **Commit clair** décrivant la correction ou la fonctionnalité, en mentionnant l'issue concernée (`fix: corrige ... (issue #ID)`).
6. **Pousser la branche** : `git push origin <branche>`
7. **Ouvrir une Pull Request** :
   - Lier l'issue (`Closes #ID`)
   - Résumer les changements et les impacts
   - Lister les tests exécutés et leur statut
8. **Revue de code** par un membre de l'équipe avant la fusion.
