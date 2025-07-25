import os
import logging
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create the app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key-change-in-production")

# Configure Flask-Mail
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT', '587'))
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME', '')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD', '')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER', 'noreply@notaire-saverys.fr')

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/about')
def about():
    return render_template('about.html')

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
            return render_template('contact.html')
        
        try:
            # Send email
            msg = Message(
                subject=f"Contact depuis le site web: {subject}",
                recipients=['franckenock78@gmail.com'],
                body=f"""
Nouveau message depuis le site web:

Nom: {name}
Email: {email}
Téléphone: {phone}
Sujet: {subject}

Message:
{message}
                """
            )
            mail.send(msg)
            
            flash('Votre message a été envoyé avec succès. Nous vous répondrons dans les plus brefs délais.', 'success')
            return redirect(url_for('contact'))
            
        except Exception as e:
            app.logger.error(f"Error sending email: {e}")
            flash('Une erreur est survenue lors de l\'envoi de votre message. Veuillez réessayer plus tard.', 'error')
    
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
