## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiement
### Prérequis
- Compte GitHub,
- Compte CircleCI,
- Compte DockerHub,
- Compte Heroku,
- Compte Sentry.

### Description
Le travail de déploiement consiste en la mise en place de l'Intégration continue/Déploiement continu 
(CI/CD), étant celle-ci composée de 4 étapes :
- Mise en place de tests via Pytest et Flake8,
- Conteneurisation de l'image Docker,
- Déploiement sur Heroku et
- Surveillance via Sentry

### Workflow
Cette CI/CD est mise en place grâce au CircleCI et à la création du fichier `config.yml`, 
dont le workflow est :
```
workflows:
  default:
    jobs:
      - build_and_test
      - build_and_push_docker_image:
          requires:
            - build_and_test
          filters:
            branches:
              only:
                - master
      - deploy_heroku:
          requires:
            - build_and_push_docker_image
          filters:
            branches:
              only:
                - master
```
Ce workflow entraîne :
- l'exécution des tests qui se fait lors de la modification de n'importe quelle branche,
- la création de l'image Docker qui se fait uniquement lors de la modification de la branche master et si 
et seulement si les tests sont validés,
- le déploiement de l'application sur Heroku qui se fait uniquement lors de la modification de la branche 
master et si et seulement si l'image Docker a été bien créée.

### Variables d'environnement
Vu que l'application sera mise en production, il faut déclarer des variables d'environnement afin de 
la sécuriser. 

Les **variables d'environnement dans CircleCI** sont :

| #   |      Variable      | Type de variable |              Description               |
|-----|:------------------:|:----------------:|:--------------------------------------:|
| 1   |  DOCKER_USERNAME   |      string      | Nom d'utilisateur dans le dépôt Docker |
| 2   | DOCKER_REPOSITORY  |      string      |          Nom du dépôt Docker           |
| 3   |  DOCKER_PASSWORD   |      string      |     Mot de passe du compte Docker      |
| 4   |   HEROKU_API_KEY   |      string      |        Clé API du compte Heroku        |
| 5   |  HEROKU_APP_NAME   |      string      |    Nom de l'application dans Heroku    |

Les **variables d'environnement dans Heroku** sont :

| #   |        Variable        | Type de variable |               Description                |
|-----|:----------------------:|:----------------:|:----------------------------------------:|
| 1   | DJANGO_SETTINGS_MODULE |      string      |      Module de configuration Django      |
| 2   |     ALLOWED_HOSTS      |   List(string)   |       Nom de l'application Heroku        |
| 3   |       SECRET_KEY       |      string      |            Clé secrète Django            |
| 4   |   WHITENOISE_ENABLED   |     boolean      | État du Whitenoise (True en production)  |
| 5   |       SENTRY_DSN       |      string      |                DSN Sentry                |

**Nota :** Pour générer une clé secrète Django, on peut passer par un générateur en ligne 
(Voir [Helpful links](#links))

## Utilisation en local
Si jamais on veut lancer l'application en local (une fois bien cloné), il faut ouvrir le fichier 
`settings.py` et remplacer :

`DEBUG = parse_bool(os.getenv('DEBUG'))`

Par : 

`DEBUG = parse_bool(os.getenv('DEBUG', 'True'))`

Ensuite, il faut s'assurer de déclarer la variable `DEBUG = False` dans Heroku.

Après, il faut ouvrir le terminal, se placer dans le dossier `../Python-OC-Lettings-FR` et taper la 
commande `python manage.py runserver`.

Finalement, il faut s'adresser au lien : `http://localhost:8000/` pour visualiser l'application en local.

Pour arrêter le serveur, il faut taper `ctrl + c` dans le terminal.

## Helpful links <a class="anchor" id="links"></a>
Dépôt Github original : https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR

Site web déployé sur Heroku : https://oc-lettings-edaucohe.herokuapp.com/

Documentation Django : https://docs.djangoproject.com/en/4.1/

Documentation Docker : https://docs.docker.com/

Documentation CircleCI : https://circleci.com/docs/

Documentation Heroku : https://devcenter.heroku.com/categories/reference

Documentation Sentry : https://docs.sentry.io/

Documentation Whitenoise : http://whitenoise.evans.io/en/stable/index.html 

Générateur en ligne de clés secrètes Django : https://miniwebtool.com/django-secret-key-generator/
