# Module `static`

## Raison d'être
Ce dossier contient les ressources statiques mises à disposition du navigateur (CSS, images, scripts autonomes). Elles sont servies directement par Flask sans passer par le moteur de templates.

## Fichiers principaux
- `style.css` : feuille de style de la calculatrice. Assure la mise en page centrée, la palette de couleurs sombre et l'apparence des boutons.

## Dépendances et hypothèses
- Les fichiers de ce dossier sont référencés via `url_for('static', filename=...)` dans les gabarits HTML.
- La structure suppose que Flask est configuré avec le dossier `static` par défaut (aucune configuration personnalisée dans `app.py`).
- Les classes CSS définies ici correspondent aux éléments présents dans `templates/index.html`.

