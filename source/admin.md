# Panel d'administration

Le panel d'administration Django est disponible sur `/admin/`.

Les modèles suivants y sont enregistrés :

- `letting.Letting`
- `letting.Address`
- `profiles.Profile`

L'enregistrement se fait simplement via `admin.site.register(...)` dans
`letting/admin.py` et `profiles/admin.py` (pas de classe `ModelAdmin`
personnalisée à ce jour).

Pour créer un compte permettant de se connecter au panel, voir [Installation
et développement local](installation.md).
