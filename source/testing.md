# Tests

Le projet utilise `pytest` avec `pytest-django`, configuré dans `setup.cfg`
(`DJANGO_SETTINGS_MODULE = oc_lettings_site.settings`).

## Organisation

Les tests sont répartis par application, chacune séparant tests unitaires et
tests d'intégration :

```text
oc_lettings_site/
└── tests.py                       # tests des gestionnaires d'erreurs 404/500

letting/
└── tests/
    ├── tests_unit.py              # tests unitaires : modèles Address, Letting
    └── tests_integration.py       # tests d'intégration : vues, résolution d'URL

profiles/
└── tests/
    ├── tests_unit.py              # tests unitaires : modèle Profile
    └── tests_integration.py       # tests d'intégration : vues, résolution d'URL
```

- **Tests unitaires** (`tests_unit.py`) : vérifient le comportement des
  modèles de manière isolée (méthodes `__str__`, validations, etc.).
- **Tests d'intégration** (`tests_integration.py`) : vérifient le
  fonctionnement des vues bout en bout (requête HTTP → réponse), y compris
  la résolution des routes.

## Jeu de données

Le fichier `fixtures.json` à la racine du projet contient des données de
test (profils, locations, adresses), utilisables pour peupler une base
locale ou pour les tests manuels :

```bash
python manage.py loaddata fixtures.json
```

## Lancer les tests

```bash
pytest
```

## Couverture de code

Le pipeline CI/CD exige une couverture minimale de **80 %** :

```bash
coverage run -m pytest
coverage report --fail-under=80
coverage html   # génère htmlcov/index.html
```
