### Flake8

#### Utilisation

Affiche les erreurs dans la console

La longeur de ligne maximale est fixée à 119

```bash
flake8 --max-line-length 119 --extend-exclude=env/
```

Création rapport HTML généré par flake8-html
```bash
flake8 --max-line-length 119 --extend-exclude=env/ --format=html --htmldir=flake8_rapport
```

