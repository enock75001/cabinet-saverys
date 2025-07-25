#!/usr/bin/env python3
"""
Site Notaire Complet - Tout en un seul fichier
Contient Python Flask + HTML + CSS intégrés
Usage: python app_complet.py
"""

import os
import logging
from flask import Flask, request, flash, redirect, url_for

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create the app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key-change-in-production")

# CSS intégré
CSS_STYLES = """
<style>
:root {
    --primary-navy: #1a365d;
    --primary-gold: #d4af37;
    --light-gold: #f7f3e9;
    --text-gray: #4a5568;
    --light-gray: #f8f9fa;
    --white: #ffffff;
}

.bg-primary { background-color: var(--primary-navy) !important; }
.btn-primary { background-color: var(--primary-navy); border-color: var(--primary-navy); }
.btn-primary:hover { background-color: #2c5282; border-color: #2c5282; }
.text-primary { color: var(--primary-navy) !important; }
.text-gold { color: var(--primary-gold) !important; }

.btn-gold {
    background-color: var(--primary-gold);
    border-color: var(--primary-gold);
    color: var(--primary-navy);
    font-weight: 600;
}
.btn-gold:hover {
    background-color: #b8941f;
    border-color: #b8941f;
    color: var(--primary-navy);
}

body {
    font-family: 'Source Sans Pro', sans-serif;
    color: var(--text-gray);
    line-height: 1.7;
    padding-top: 80px;
}

h1, h2, h3, h4, h5, h6 {
    font-family: 'Playfair Display', serif;
    font-weight: 700;
    color: var(--primary-navy);
}

.navbar-brand {
    font-family: 'Playfair Display', serif;
    font-weight: 700;
}

.hero-section {
    background: linear-gradient(135deg, var(--primary-navy) 0%, #2c5282 50%, #1a365d 100%);
    min-height: 60vh;
}

.service-card {
    background: white;
    border-radius: 10px;
    padding: 2rem;
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    transition: transform 0.3s ease;
    border: 1px solid #e2e8f0;
}

.service-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(0,0,0,0.15);
}

.contact-form-card {
    background: white;
    border-radius: 10px;
    padding: 2rem;
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    border: 1px solid #e2e8f0;
}

.contact-info-card {
    background: var(--light-gold);
    border-radius: 10px;
    padding: 2rem;
    height: 100%;
}
</style>
"""

# Template de base HTML intégré
def render_base_template(title="Maître Marc Saverys - Notaire", content="", active_page=""):
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Font Awesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Source+Sans+Pro:wght@300;400;600&display=swap" rel="stylesheet">
    
    {CSS_STYLES}
    
    <meta name="description" content="Étude notariale de Maître Marc Saverys à Jeu-les-Bois. Services notariaux complets: immobilier, famille, succession, entreprise.">
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary fixed-top shadow-lg">
        <div class="container">
            <a class="navbar-brand d-flex align-items-center" href="/">
                <div class="logo-icon me-3">
                    <i class="fas fa-balance-scale fs-4 text-gold"></i>
                </div>
                <div>
                    <div class="fw-bold">Maître Marc Saverys</div>
                    <small class="text-gold opacity-75">Notaire</small>
                </div>
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link {'active' if active_page == 'index' else ''}" href="/">Accueil</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link {'active' if active_page == 'services' else ''}" href="/services">Services</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link {'active' if active_page == 'about' else ''}" href="/about">À propos</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link {'active' if active_page == 'contact' else ''}" href="/contact">Contact</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Messages -->
    <div class="container mt-5 pt-3">
        {flash_messages()}
    </div>

    <!-- Main Content -->
    <main>
        {content}
    </main>

    <!-- Footer -->
    <footer class="bg-dark text-light py-5 mt-5">
        <div class="container">
            <div class="row">
                <div class="col-md-4 mb-4">
                    <h5 class="text-gold">Étude Notariale</h5>
                    <p>Maître Marc Saverys<br>
                    Notaire à Jeu-les-Bois<br>
                    Expertise juridique depuis 2009</p>
                </div>
                <div class="col-md-4 mb-4">
                    <h5 class="text-gold">Contact</h5>
                    <p><i class="fas fa-map-marker-alt me-2"></i>123 Rue de la République<br>
                    36240 Jeu-les-Bois</p>
                    <p><i class="fas fa-phone me-2"></i>02 54 XX XX XX</p>
                    <p><i class="fas fa-envelope me-2"></i>contact@notaire-saverys.fr</p>
                </div>
                <div class="col-md-4 mb-4">
                    <h5 class="text-gold">Horaires</h5>
                    <p>Lundi - Vendredi : 9h00 - 18h00<br>
                    Samedi : 9h00 - 12h00<br>
                    Sur rendez-vous uniquement</p>
                </div>
            </div>
            <hr class="border-gold">
            <div class="row">
                <div class="col-md-6">
                    <p>&copy; 2025 Maître Marc Saverys - Tous droits réservés</p>
                </div>
                <div class="col-md-6 text-end">
                    <p>Mentions légales | Confidentialité</p>
                </div>
            </div>
        </div>
    </footer>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>"""

def flash_messages():
    """Récupère et affiche les messages flash"""
    from flask import get_flashed_messages
    messages = get_flashed_messages(with_categories=True)
    if not messages:
        return ""
    
    html = ""
    for category, message in messages:
        alert_type = 'danger' if category == 'error' else 'success'
        html += f'''<div class="alert alert-{alert_type} alert-dismissible fade show" role="alert">
            {message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        </div>'''
    return html

@app.route('/')
def index():
    content = """
    <!-- Hero Section -->
    <section class="hero-section bg-primary text-white">
        <div class="container">
            <div class="row align-items-center py-5">
                <div class="col-lg-6">
                    <div class="badge bg-gold text-navy mb-3 px-3 py-2 rounded-pill fw-semibold">
                        <i class="fas fa-star me-2"></i>15+ années d'expérience
                    </div>
                    <h1 class="display-4 fw-bold mb-4 text-white">Maître Marc Saverys</h1>
                    <h2 class="h3 text-gold mb-4">
                        <i class="fas fa-balance-scale me-2"></i>Notaire à Jeu-les-Bois
                    </h2>
                    <p class="lead mb-4">
                        Expertise juridique et accompagnement personnalisé pour tous vos projets immobiliers, 
                        familiaux et patrimoniaux depuis plus de 15 ans.
                    </p>
                    <div class="d-flex flex-wrap gap-3 mb-4">
                        <a href="/contact" class="btn btn-gold btn-lg shadow-lg">
                            <i class="fas fa-calendar-check me-2"></i>Prendre rendez-vous
                        </a>
                        <a href="/services" class="btn btn-outline-light btn-lg">
                            <i class="fas fa-briefcase me-2"></i>Nos services
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Services Overview -->
    <section class="py-5">
        <div class="container">
            <div class="row">
                <div class="col-lg-8 mx-auto text-center mb-5">
                    <h2 class="display-5 fw-bold mb-4">Nos domaines d'expertise</h2>
                    <p class="lead text-muted">
                        Une approche professionnelle et humaine pour vous accompagner dans tous vos projets juridiques
                    </p>
                </div>
            </div>
            <div class="row g-4">
                <div class="col-md-6 col-lg-3">
                    <div class="service-card text-center h-100">
                        <div class="service-icon mb-3">
                            <i class="fas fa-home fs-1 text-primary"></i>
                        </div>
                        <h4>Immobilier</h4>
                        <p class="text-muted">Ventes, acquisitions, prêts immobiliers et copropriété</p>
                    </div>
                </div>
                <div class="col-md-6 col-lg-3">
                    <div class="service-card text-center h-100">
                        <div class="service-icon mb-3">
                            <i class="fas fa-users fs-1 text-primary"></i>
                        </div>
                        <h4>Droit de la famille</h4>
                        <p class="text-muted">Mariages, PACS, divorces et régimes matrimoniaux</p>
                    </div>
                </div>
                <div class="col-md-6 col-lg-3">
                    <div class="service-card text-center h-100">
                        <div class="service-icon mb-3">
                            <i class="fas fa-file-alt fs-1 text-primary"></i>
                        </div>
                        <h4>Successions</h4>
                        <p class="text-muted">Testaments, donations et règlements successoraux</p>
                    </div>
                </div>
                <div class="col-md-6 col-lg-3">
                    <div class="service-card text-center h-100">
                        <div class="service-icon mb-3">
                            <i class="fas fa-briefcase fs-1 text-primary"></i>
                        </div>
                        <h4>Droit des affaires</h4>
                        <p class="text-muted">Création d'entreprises, cessions et baux commerciaux</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
    """
    return render_base_template(content=content, active_page="index")

@app.route('/services')
def services():
    content = """
    <section class="py-5">
        <div class="container">
            <div class="row">
                <div class="col-lg-8 mx-auto text-center mb-5">
                    <h1 class="display-4 fw-bold mb-4">Nos Services</h1>
                    <p class="lead text-muted">
                        Une expertise complète dans tous les domaines du droit notarial 
                        pour vous accompagner dans vos projets de vie
                    </p>
                </div>
            </div>

            <div class="row mb-5">
                <div class="col-lg-6 mb-4">
                    <div class="service-card h-100">
                        <div class="text-center mb-3">
                            <i class="fas fa-home fs-1 text-primary mb-3"></i>
                            <h2>Droit Immobilier</h2>
                        </div>
                        <h5>Ventes et Acquisitions</h5>
                        <ul class="list-unstyled mb-4">
                            <li><i class="fas fa-check text-success me-2"></i>Rédaction et signature des avant-contrats</li>
                            <li><i class="fas fa-check text-success me-2"></i>Négociation des conditions de vente</li>
                            <li><i class="fas fa-check text-success me-2"></i>Vérification des titres de propriété</li>
                            <li><i class="fas fa-check text-success me-2"></i>Calcul et perception des droits et taxes</li>
                        </ul>
                        
                        <h5>Financement</h5>
                        <ul class="list-unstyled">
                            <li><i class="fas fa-check text-success me-2"></i>Constitution de garanties hypothécaires</li>
                            <li><i class="fas fa-check text-success me-2"></i>Mainlevées d'hypothèques</li>
                            <li><i class="fas fa-check text-success me-2"></i>Renégociation de prêts immobiliers</li>
                        </ul>
                    </div>
                </div>
                <div class="col-lg-6 mb-4">
                    <div class="service-card h-100">
                        <div class="text-center mb-3">
                            <i class="fas fa-users fs-1 text-primary mb-3"></i>
                            <h2>Droit de la Famille</h2>
                        </div>
                        <h5>Union et Mariage</h5>
                        <ul class="list-unstyled mb-4">
                            <li><i class="fas fa-check text-success me-2"></i>Contrats de mariage</li>
                            <li><i class="fas fa-check text-success me-2"></i>Conventions de PACS</li>
                            <li><i class="fas fa-check text-success me-2"></i>Changement de régime matrimonial</li>
                            <li><i class="fas fa-check text-success me-2"></i>Adoption simple et plénière</li>
                        </ul>
                        
                        <h5>Séparation et Divorce</h5>
                        <ul class="list-unstyled">
                            <li><i class="fas fa-check text-success me-2"></i>Divorce par consentement mutuel</li>
                            <li><i class="fas fa-check text-success me-2"></i>Liquidation de régimes matrimoniaux</li>
                            <li><i class="fas fa-check text-success me-2"></i>Partage des biens</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </section>
    """
    return render_base_template(title="Services - Maître Marc Saverys", content=content, active_page="services")

@app.route('/about')
def about():
    content = """
    <section class="py-5">
        <div class="container">
            <div class="row align-items-center mb-5">
                <div class="col-lg-4 text-center mb-4 mb-lg-0">
                    <i class="fas fa-user-tie fs-1 text-primary"></i>
                    <p class="text-muted mt-3">Maître Marc Saverys</p>
                </div>
                <div class="col-lg-8">
                    <h1 class="display-4 fw-bold mb-4">Maître Marc Saverys</h1>
                    <h2 class="h3 text-primary mb-4">Notaire à Jeu-les-Bois</h2>
                    <p class="lead text-muted mb-4">
                        Avec plus de 15 ans d'expérience, j'ai fondé mon étude sur des valeurs de rigueur, 
                        de disponibilité et de confiance.
                    </p>
                    <p class="mb-4">
                        Notre mission est de vous offrir une sécurité juridique optimale en vous fournissant 
                        des conseils éclairés et en rédigeant des actes authentiques incontestables, 
                        adaptés à chaque situation personnelle et professionnelle.
                    </p>
                    <p class="mb-4 text-primary fw-bold">
                        Votre partenaire juridique pour la vie.
                    </p>
                    <div class="d-flex flex-wrap gap-2">
                        <span class="badge bg-primary fs-6">Droit Immobilier</span>
                        <span class="badge bg-primary fs-6">Droit de la Famille</span>
                        <span class="badge bg-primary fs-6">Successions</span>
                        <span class="badge bg-primary fs-6">Droit des Affaires</span>
                    </div>
                </div>
            </div>
        </div>
    </section>
    """
    return render_base_template(title="À propos - Maître Marc Saverys", content=content, active_page="about")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        # Basic validation
        if not all([name, email, subject, message]):
            flash('Tous les champs obligatoires doivent être remplis.', 'error')
        else:
            flash('Votre message a été envoyé avec succès. Nous vous répondrons dans les plus brefs délais.', 'success')
            return redirect(url_for('contact'))
    
    content = """
    <section class="py-5">
        <div class="container">
            <div class="row">
                <div class="col-lg-8 mx-auto text-center mb-5">
                    <h1 class="display-4 fw-bold mb-4">Contactez-nous</h1>
                    <p class="lead text-muted">
                        Nous sommes à votre disposition pour répondre à vos questions 
                        et vous accompagner dans vos démarches juridiques
                    </p>
                </div>
            </div>

            <div class="row">
                <div class="col-lg-8 mb-5">
                    <div class="contact-form-card">
                        <h2 class="h3 mb-4">Envoyez-nous un message</h2>
                        <form method="POST" action="/contact">
                            <div class="row">
                                <div class="col-md-6 mb-3">
                                    <label for="name" class="form-label">Nom et Prénom *</label>
                                    <input type="text" class="form-control" id="name" name="name" required>
                                </div>
                                <div class="col-md-6 mb-3">
                                    <label for="email" class="form-label">Email *</label>
                                    <input type="email" class="form-control" id="email" name="email" required>
                                </div>
                            </div>
                            <div class="row">
                                <div class="col-md-6 mb-3">
                                    <label for="phone" class="form-label">Téléphone</label>
                                    <input type="tel" class="form-control" id="phone" name="phone">
                                </div>
                                <div class="col-md-6 mb-3">
                                    <label for="subject" class="form-label">Sujet *</label>
                                    <select class="form-select" id="subject" name="subject" required>
                                        <option value="">Choisissez un sujet</option>
                                        <option value="Demande de rendez-vous">Demande de rendez-vous</option>
                                        <option value="Droit immobilier">Droit immobilier</option>
                                        <option value="Droit de la famille">Droit de la famille</option>
                                        <option value="Successions">Successions</option>
                                        <option value="Droit des affaires">Droit des affaires</option>
                                        <option value="Autre">Autre</option>
                                    </select>
                                </div>
                            </div>
                            <div class="mb-3">
                                <label for="message" class="form-label">Message *</label>
                                <textarea class="form-control" id="message" name="message" rows="6" required 
                                          placeholder="Décrivez votre situation ou votre demande..."></textarea>
                            </div>
                            <button type="submit" class="btn btn-primary btn-lg">
                                <i class="fas fa-paper-plane me-2"></i>Envoyer le message
                            </button>
                        </form>
                    </div>
                </div>

                <div class="col-lg-4">
                    <div class="contact-info-card">
                        <h3 class="h4 mb-4"><i class="fas fa-map-marker-alt me-2 text-primary"></i>Notre Étude</h3>
                        <p><strong>Maître Marc Saverys</strong><br>
                        Notaire<br>
                        123 Rue de la République<br>
                        36240 Jeu-les-Bois</p>
                        
                        <h4 class="h5 mb-3 mt-4"><i class="fas fa-phone me-2 text-primary"></i>Téléphone</h4>
                        <p>02 54 XX XX XX</p>
                        
                        <h4 class="h5 mb-3 mt-4"><i class="fas fa-envelope me-2 text-primary"></i>Email</h4>
                        <p>contact@notaire-saverys.fr</p>
                        
                        <h4 class="h5 mb-3 mt-4"><i class="fas fa-clock me-2 text-primary"></i>Horaires</h4>
                        <p>Lundi - Vendredi : 9h00 - 18h00<br>
                        Samedi : 9h00 - 12h00<br>
                        <em>Sur rendez-vous uniquement</em></p>
                    </div>
                </div>
            </div>
        </div>
    </section>
    """
    return render_base_template(title="Contact - Maître Marc Saverys", content=content, active_page="contact")

if __name__ == '__main__':
    # Configuration pour le développement
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    
    print("🏛️ Site Notaire - Tout en un seul fichier")
    print(f"📍 Port: {port}")
    print("🌐 Accès: http://localhost:5000")
    
    app.run(host='0.0.0.0', port=port, debug=debug)