# Architecture

## Applications Django

Chaque application suit la structure standard Django : `models.py`,
`views.py`, `urls.py`, `admin.py`, `apps.py`, `migrations/`, `templates/`,
et un dossier `tests/`.

Le projet est composé de trois applications :

- **`oc_lettings_site`** est l'application racine. Elle reçoit toutes les
  requêtes en premier (`oc_lettings_site.urls`) et affiche la page
  d'accueil. Elle délègue ensuite aux applications `letting` et `profiles`
  selon le préfixe d'URL (`/lettings/*` ou `/profiles/*`), et prend en
  charge les pages d'erreur 404/500 ainsi que le panel d'administration
  Django (`/admin/*`).
- **`letting`** gère les locations : ses vues lisent et affichent les
  modèles `Letting` et `Address`.
- **`profiles`** gère les profils utilisateurs : ses vues lisent et
  affichent le modèle `Profile`, lié à un `User` Django.

Voir [Applications](apps.md) pour le détail des modèles et vues de chaque
application, et [Routes](urls.md) pour la liste complète des URLs.

## Journalisation

Chaque application (`letting`, `profiles`, `oc_lettings_site`) possède son
propre logger, configuré dans `oc_lettings_site/settings.py` (niveau `INFO`,
sortie console). Les accès aux pages et les erreurs 404/500 sont journalisés.

## Suivi des erreurs

`config/sentry.py` initialise Sentry si la variable d'environnement
`SENTRY_SDK` (DSN) est définie. Le taux d'échantillonnage des traces est de
100 % (`traces_sample_rate=1.0`).
