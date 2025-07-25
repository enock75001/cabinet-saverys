# Guide d'Installation - Site Notaire

## Téléchargement
Votre site est disponible dans l'archive : **notaire-saverys-website.tar.gz**

## Étapes d'installation

### 1. Extraire l'archive
```bash
tar -xzf notaire-saverys-website.tar.gz
cd notaire-saverys-website
```

### 2. Installer Python et les dépendances
```bash
# Sur Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip

# Installer les dépendances
pip3 install flask flask-mail gunicorn
```

### 3. Configuration des emails
Créer un fichier `.env` avec :
```bash
SESSION_SECRET=votre-cle-secrete-unique
MAIL_USERNAME=votre-email@gmail.com
MAIL_PASSWORD=mot-de-passe-application-gmail
```

### 4. Lancer le site
```bash
# Mode développement
python3 app.py

# Mode production
gunicorn --bind 0.0.0.0:5000 main:app
```

Le site sera accessible sur : http://localhost:5000

## Configuration Gmail
1. Aller dans les paramètres de votre compte Gmail
2. Activer l'authentification à 2 facteurs
3. Générer un "Mot de passe d'application" 
4. Utiliser ce mot de passe dans MAIL_PASSWORD

## Hébergement recommandé
- **Replit** (le plus simple)
- **Heroku** (gratuit avec limitations)
- **DigitalOcean** (5$/mois)
- **PythonAnywhere** (gratuit avec limitations)

Votre site est prêt à être déployé !