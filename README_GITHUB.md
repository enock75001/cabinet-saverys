# Site Notaire Professionnel

Site web professionnel pour étude notariale, développé avec Flask et déployable sur multiple plateformes.

## 🌟 Fonctionnalités

- **Design Responsive** : Interface moderne adaptée à tous les appareils
- **Formulaire de Contact** : Système d'envoi d'emails intégré
- **Pages Professionnelles** : Accueil, Services, À propos, Contact
- **Sécurisé** : Configuration SSL et gestion sécurisée des données
- **Multilingue** : Support français avec possibilité d'extension

## 🚀 Technologies

- **Backend** : Flask (Python)
- **Frontend** : HTML5, CSS3, Bootstrap
- **Email** : Flask-Mail avec SMTP Gmail
- **Serveur** : Gunicorn
- **Déploiement** : Compatible Heroku, DigitalOcean, Vercel, Netlify

## 📦 Installation

### 1. Cloner le projet
```bash
git clone https://github.com/[votre-username]/site-notaire.git
cd site-notaire
```

### 2. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 3. Configuration
Créer un fichier `.env` :
```env
SESSION_SECRET=votre-cle-secrete-unique
MAIL_USERNAME=votre-email@gmail.com
MAIL_PASSWORD=mot-de-passe-application-gmail
MAIL_DEFAULT_SENDER=contact@votre-domaine.fr
```

### 4. Lancer l'application
```bash
# Développement
python app.py

# Production
gunicorn --bind 0.0.0.0:5000 main:app
```

## 🌐 Déploiement

### Heroku
```bash
git push heroku main
```

### DigitalOcean App Platform
1. Connecter votre repository GitHub
2. Configurer les variables d'environnement
3. Déployer automatiquement

### Vercel/Netlify
Compatible avec les fonctions serverless Python.

## 📧 Configuration Email Gmail

1. Activer l'authentification à 2 facteurs
2. Générer un "Mot de passe d'application"
3. Utiliser ce mot de passe dans `MAIL_PASSWORD`

## 📁 Structure du Projet

```
/
├── app.py              # Application Flask principale
├── main.py             # Point d'entrée Gunicorn
├── templates/          # Templates Jinja2
│   ├── base.html       # Template de base
│   ├── index.html      # Page d'accueil
│   ├── services.html   # Services notariaux
│   ├── about.html      # À propos
│   └── contact.html    # Formulaire de contact
├── static/             # Assets statiques
│   ├── css/style.css   # Styles personnalisés
│   ├── js/main.js      # JavaScript
│   └── images/         # Images SVG
├── requirements.txt    # Dépendances Python
└── README.md          # Documentation
```

## 🎨 Personnalisation

- **Couleurs** : Modifier les variables CSS dans `static/css/style.css`
- **Contenu** : Éditer les templates HTML dans `templates/`
- **Logo** : Remplacer les images SVG dans `static/images/`
- **Contact** : Modifier l'email destinataire dans `app.py` ligne 53

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou soumettre une pull request.

## 📞 Support

Pour toute question, contactez : [votre-email@domain.com]

---

🏛️ **Site Notaire Professionnel** - Solution web moderne pour études notariales