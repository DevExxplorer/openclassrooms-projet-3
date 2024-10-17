# Openclassrooms - Projet 4 : Développez un programme logiciel en Python
***
***

## Description
***
Ce projet est une application d'organisation de tournoi d'échecs

## Installation
***
Activez l'environnement et installez les packages à l'aide du fichier requirements.txt :
```
$ python -m venv <environment name>
$ source <environment name>/bin/activate
$ pip install -r requirements.txt
```

## Utilisation
***
Pour lancer l'application:
```
$ python main.py
```

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

