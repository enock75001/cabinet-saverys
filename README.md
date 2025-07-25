# Site Web Notaire - Maître Marc Saverys

## Description
Site web professionnel pour l'étude notariale de Maître Marc Saverys à Jeu-les-Bois, France.

## Fonctionnalités
- Site web responsive avec Bootstrap 5
- Formulaire de contact avec envoi d'emails
- Images SVG personnalisées et professionnelles
- Design moderne avec animations CSS
- Pages : Accueil, Services, À propos, Contact

## Technologies utilisées
- **Backend** : Flask (Python)
- **Frontend** : HTML5, CSS3, JavaScript
- **Framework CSS** : Bootstrap 5.3.0
- **Icons** : Font Awesome 6.4.0
- **Fonts** : Google Fonts (Playfair Display, Source Sans Pro)
- **Email** : Flask-Mail avec SMTP Gmail

## Installation et déploiement

### Prérequis
- Python 3.11+
- pip ou uv pour la gestion des dépendances

### Installation locale
1. Extraire l'archive
2. Installer les dépendances :
   ```bash
   pip install flask flask-mail gunicorn
   ```

3. Configurer les variables d'environnement :
   ```bash
   export SESSION_SECRET="votre-clé-secrète"
   export MAIL_USERNAME="votre-email@gmail.com"
   export MAIL_PASSWORD="mot-de-passe-application-gmail"
   ```

4. Lancer l'application :
   ```bash
   python app.py
   ```
   Ou avec Gunicorn pour la production :
   ```bash
   gunicorn --bind 0.0.0.0:5000 main:app
   ```

### Configuration Email
Pour que le formulaire de contact fonctionne :
1. Créer un mot de passe d'application Gmail
2. Configurer les variables MAIL_USERNAME et MAIL_PASSWORD
3. Les emails seront envoyés vers franckenock78@gmail.com

## Structure du projet
```
/
├── app.py              # Application Flask principale
├── main.py             # Point d'entrée pour Gunicorn
├── templates/          # Templates Jinja2
│   ├── base.html       # Template de base
│   ├── index.html      # Page d'accueil
│   ├── services.html   # Page des services
│   ├── about.html      # Page à propos
│   └── contact.html    # Page de contact
├── static/             # Fichiers statiques
│   ├── css/
│   │   └── style.css   # Styles personnalisés
│   ├── js/
│   │   └── main.js     # JavaScript personnalisé
│   └── images/         # Images SVG
└── pyproject.toml      # Configuration des dépendances
```

## Personnalisation
- Modifier les informations de contact dans les templates
- Ajuster les couleurs dans les variables CSS (style.css)
- Remplacer les images SVG selon vos besoins
- Adapter le contenu des pages dans les templates HTML

## Déploiement
Le site est prêt pour le déploiement sur :
- Replit Deployments (recommandé)
- Heroku
- DigitalOcean App Platform
- Tout serveur compatible Python/Flask

## Support
Contact : franckenock78@gmail.com

---
© 2025 Étude Notariale Maître Marc Saverys