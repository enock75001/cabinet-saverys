# 🏛️ Site Notaire - Dossier Complet

Ce dossier contient tous les fichiers nécessaires pour votre site notaire professionnel.

## 📁 Structure du dossier

```
site-notaire/
├── app.py              # Application Flask principale
├── main.py             # Point d'entrée pour serveur
├── run.py              # Script de lancement simple
├── requirements.txt    # Dépendances Python
├── pyproject.toml      # Configuration du projet
├── README.md           # Documentation détaillée
├── INSTALLATION.md     # Guide d'installation
├── templates/          # Pages HTML
│   ├── base.html       # Template de base
│   ├── index.html      # Page d'accueil
│   ├── services.html   # Services notariaux
│   ├── about.html      # À propos
│   └── contact.html    # Formulaire de contact
└── static/             # Fichiers statiques
    ├── css/           # Styles
    ├── js/            # JavaScript
    └── images/        # Images SVG
```

## 🚀 Lancement rapide

### Option 1 : Script simple
```bash
cd site-notaire
pip install -r requirements.txt
python run.py
```

### Option 2 : Serveur production
```bash
cd site-notaire
pip install -r requirements.txt
gunicorn --bind 0.0.0.0:5000 main:app
```

## 📧 Configuration email

Créer un fichier `.env` dans le dossier :
```env
SESSION_SECRET=votre-cle-secrete
MAIL_USERNAME=votre-email@gmail.com
MAIL_PASSWORD=mot-de-passe-application
```

## 📦 Déploiement

Ce dossier est prêt pour :
- Upload direct sur serveur
- Déploiement Heroku/Vercel
- Archive ZIP pour livraison client

---

✨ **Site professionnel complet dans un seul dossier !**