# Module `templates`

## Raison d'être
Ce répertoire regroupe les gabarits HTML utilisés par Flask pour générer les réponses côté serveur. Chaque fichier correspond à une page rendue au navigateur de l'utilisateur.

## Fichiers principaux
- `index.html` : interface principale de la calculatrice. Définit la structure de la page, les boutons de saisie et un petit script JavaScript pour gérer l'affichage des chiffres et opérateurs.

## Dépendances et hypothèses
- Les fichiers HTML sont rendus via `flask.render_template` dans `app.py`.
- Les gabarits supposent l'existence des ressources statiques exposées par Flask (`url_for('static', ...)`) et du style défini dans `static/style.css`.
- Aucun autre moteur de template n'est prévu : on reste sur Jinja2 tel qu'embarqué par Flask.

