# Module utils

Rôle
----
Le répertoire `utils/` contient des fonctions utilitaires réutilisables pour
le projet. Actuellement il fournit les opérations arithmétiques de base
utilisées par l'application web.

Fichiers principaux
-------------------
- `operators.py` : Implémentations simples des opérations `add`, `subtract`,
  `multiply` et `divide`. Chaque fonction accepte deux nombres et renvoie
  le résultat numérique.

Dépendances / hypothèses
-------------------------
- Les fonctions s'attendent à des types numériques (float/int). La validation
  des entrées (par ex. conversion depuis une chaîne) est faite dans le
  module appelant (`app.py`).

Utilisation
---------
Importer directement les fonctions nécessaires depuis `utils/operators.py`.

Exemple:
```
from operators import add
result = add(2, 3)
```
