# 📚 Guide d'Export vers GitHub

## 🚀 Méthode Replit (Recommandée)

### Étape 1 : Export automatique depuis Replit
1. **Dans votre Replit :**
   - Cliquez sur les trois points (...) en haut à droite
   - Sélectionnez **"Export to GitHub"**
   - Connectez votre compte GitHub si demandé

2. **Configuration du repository :**
   - Nom : `site-notaire-professionnel`
   - Description : "Site web professionnel pour étude notariale"
   - Visibilité : Public ou Privé selon votre choix

### Étape 2 : Après l'export
Le repository contiendra automatiquement tous vos fichiers :
- ✅ Code source (app.py, main.py)
- ✅ Templates HTML
- ✅ Fichiers CSS/JS
- ✅ Configuration (.gitignore)
- ✅ Documentation (README)

## 🔧 Méthode Manuelle (Alternative)

### Si l'export automatique ne fonctionne pas :

1. **Créer un nouveau repository sur GitHub :**
   - Aller sur https://github.com/new
   - Nom : `site-notaire-professionnel`
   - Cocher "Add README file"

2. **Télécharger le code depuis Replit :**
   - Utiliser le bouton "Download as ZIP"
   - Extraire le fichier ZIP

3. **Upload sur GitHub :**
   - Glisser-déposer les fichiers dans votre repository
   - Ou utiliser "Upload files" sur GitHub

## 📁 Fichiers à inclure dans GitHub

### ✅ Fichiers essentiels :
- `app.py` - Application Flask principale
- `main.py` - Point d'entrée
- `templates/` - Tous les templates HTML
- `static/` - CSS, JS, images
- `requirements_github.txt` - Dépendances (à renommer en requirements.txt)
- `README_GITHUB.md` - Documentation (à renommer en README.md)
- `.gitignore` - Fichiers à ignorer

### ❌ Fichiers à exclure :
- `__pycache__/` - Cache Python
- `.replit` - Configuration Replit
- `uv.lock` - Lock file Replit
- `notaire-saverys-website.tar.gz` - Archive

## 🌐 Déploiement depuis GitHub

### Option 1 : Heroku
```bash
# Après avoir cloné votre repository
git clone https://github.com/[username]/site-notaire-professionnel.git
cd site-notaire-professionnel

# Créer une app Heroku
heroku create mon-site-notaire

# Configurer les variables d'environnement
heroku config:set SESSION_SECRET=votre-cle-secrete
heroku config:set MAIL_USERNAME=votre-email@gmail.com
heroku config:set MAIL_PASSWORD=mot-de-passe-app

# Déployer
git push heroku main
```

### Option 2 : Vercel
1. Connecter votre repository GitHub sur vercel.com
2. Ajouter les variables d'environnement
3. Déployer automatiquement

### Option 3 : DigitalOcean App Platform
1. Créer une nouvelle app
2. Connecter votre repository GitHub
3. Configurer les variables d'environnement
4. Déployer

## 🔐 Variables d'Environnement Requises

Pour tous les déploiements, configurez :
```
SESSION_SECRET=cle-secrete-unique-32-caracteres
MAIL_USERNAME=votre-email@gmail.com
MAIL_PASSWORD=mot-de-passe-application-gmail
MAIL_DEFAULT_SENDER=contact@votre-domaine.fr
```

## 📞 Après l'Export

1. **Renommer les fichiers :**
   - `requirements_github.txt` → `requirements.txt`
   - `README_GITHUB.md` → `README.md`

2. **Personnaliser :**
   - Modifier l'email de contact dans `app.py`
   - Adapter le contenu dans les templates
   - Personnaliser les couleurs CSS

3. **Tester localement :**
   ```bash
   pip install -r requirements.txt
   python app.py
   ```

## 🎯 URL de votre site après déploiement

- **Heroku :** `https://mon-site-notaire.herokuapp.com`
- **Vercel :** `https://site-notaire-professionnel.vercel.app`
- **DigitalOcean :** `https://site-notaire-xxxx.ondigitalocean.app`

---

🏛️ **Votre site notaire sera accessible 24h/24 avec une URL professionnelle !**