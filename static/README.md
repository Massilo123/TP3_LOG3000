# Module static

Rôle
----
Le répertoire `static/` contient les ressources statiques servies par
l'application Flask (feuilles de style, images, scripts côté client).

Fichiers principaux
-------------------
- `style.css` : styles CSS utilisés par la page principale.

Dépendances / hypothèses
-------------------------
- Ces fichiers sont destinés à être servis tels quels par Flask via la
  configuration par défaut (`static/`), sans pré-processing.

Remarques
--------
Gardez les fichiers statiques simples. Pour un projet plus large, envisager
de scinder `css`, `js`, et `img` dans des sous-répertoires.
