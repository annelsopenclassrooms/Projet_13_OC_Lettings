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

# Surveillance et journalisation avec Sentry

Pour améliorer l’observabilité et le suivi des erreurs, le projet intègre **Sentry**. Cela permet de capturer automatiquement les exceptions inattendues, les problèmes de performance et les logs personnalisés.

## Installation et configuration

Dans l’environnement virtuel, installez Sentry et python-dotenv :

```bash
pip install "sentry-sdk[django]" python-dotenv
```

Dans `oc_lettings_site/settings.py` :

```python
import os
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

SENTRY_DSN = os.getenv("SENTRY_DSN")  # récupéré depuis les variables d'environnement

if SENTRY_DSN:
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[DjangoIntegration()],
        traces_sample_rate=1.0,
        send_default_pii=True,
    )

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {"class": "logging.StreamHandler"},
    },
    "root": {"handlers": ["console"], "level": "INFO"},
    "loggers": {
        "django": {"handlers": ["console"], "level": "INFO", "propagate": True},
        "oc_lettings_site": {"handlers": ["console"], "level": "DEBUG", "propagate": False},
    },
}
```

Ajoutez la variable `SENTRY_DSN` dans votre fichier `.env` (ne jamais le committer) :

```bash
SENTRY_DSN=https://<votre-cle>@oXXXX.ingest.sentry.io/YYYY
```

## Bonnes pratiques

- Utilisez le module `logging` dans les fonctions critiques et les blocs `try/except`.
- En cas d’erreur, envoyez l’exception à Sentry avec :

```python
import sentry_sdk
sentry_sdk.capture_exception(e)
```

- Vérifiez que les logs apparaissent à la fois dans la console et dans le dashboard Sentry.

## Vérification

Pour tester l’intégration, vous pouvez lever une exception manuellement :

```python
raise Exception("Test Sentry")
```

L’erreur doit ensuite apparaître dans l’interface Sentry.

## Politique de logs et Sentry

- **Console** :
  - Tous les logs à partir du niveau `INFO` sont affichés.
  - Utile pour le suivi en local et la consultation des logs en production.

- **Sentry** :
  - Seuls les logs de niveau `ERROR` et `CRITICAL` sont envoyés.
  - Capture automatiquement toutes les exceptions Django non gérées grâce à `DjangoIntegration`.
  - Les informations personnelles minimales (PII), comme l’utilisateur connecté et l’adresse IP, sont incluses (`send_default_pii=True`).

- **Applications** :
  - `lettings` et `profiles` : logs à partir du niveau `INFO`.
  - `django` : logs à partir du niveau `WARNING`.

👉 En résumé : **tous les détails apparaissent dans la console, mais seuls les incidents critiques sont envoyés à Sentry**.

## Déploiement

### Récapitulatif du fonctionnement

Le déploiement utilise **GitHub Actions** et **Render** :  
1. Lancement des tests (`flake8`, `pytest`) avec couverture minimale de 80 %.  
2. Construction et push d’une image Docker sur **Docker Hub**.  
3. Déploiement sur Render basé sur l’image Docker.  

Seules les modifications poussées sur la branche **master** déclenchent la conteneurisation.  
Le déploiement sur Render est déclenché manuellement après la construction de l’image Docker.  
Les autres branches (ex: `dev`) ne déclenchent que les tests et linting.

### Configuration requise

#### Secrets GitHub Actions
À définir dans **Repository → Settings → Secrets and variables → Actions** :
- `SECRET_KEY` : clé secrète Django  
- `SENTRY_DSN` : identifiant de Sentry  
- `ALLOWED_HOSTS` : domaines autorisés  
- `DOCKER_USERNAME` : identifiant Docker Hub  
- `DOCKER_PASSWORD` : mot de passe ou token Docker Hub  

#### Variables d’environnement Render
À définir dans l’onglet **Environment** du service Render :
- `SECRET_KEY`  
- `SENTRY_DSN`  
- `ALLOWED_HOSTS`  

### Étapes de déploiement

1. Pousser vos modifications sur la branche **master**.  
2. Vérifier dans l’onglet **Actions** de GitHub :  
   - Tests réussis  
   - Image Docker construite et poussée sur Docker Hub  
3. Déclencher manuellement le déploiement depuis le dashboard **Render**.  
4. Vérifier que le service a redémarré et tester l’URL de production.  

### Bonnes pratiques

- Ne jamais committer de secrets dans le code.  
- Utiliser `.env` et `python-dotenv` en local.  
- Vérifier les fichiers statiques avec :  
  ```bash
  python manage.py collectstatic