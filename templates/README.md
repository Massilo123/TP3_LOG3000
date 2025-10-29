# Module templates

Rôle
----
Le répertoire `templates/` contient les gabarits HTML rendus par Flask.

Fichiers principaux
-------------------
- `index.html` : Page principale qui affiche le champ de saisie et le résultat
  renvoyé par le calcul.

Dépendances / hypothèses
-------------------------
- Les templates sont rendues via `render_template` et attendent que
  l'application fournisse une variable `result` (chaîne ou nombre).

Remarques
--------
Les templates actuelles sont simples et n'utilisent pas d'héritage Jinja.
Pour un projet évolutif, envisager un layout de base (`base.html`).
