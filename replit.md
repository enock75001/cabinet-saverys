# Replit MD - Notary Office Website

## Overview

This is a French notary office website for "Maître Marc Saverys" located in Jeu-les-Bois, France built with Flask. The application provides a professional web presence showcasing notarial services, attorney information, and contact functionality. The site is built as a traditional server-side rendered application with Bootstrap for styling and includes email functionality for client inquiries.

## User Preferences

- Preferred communication style: Simple, everyday language.
- Notary name: Maître Marc Saverys
- Location: 36120 Jeu-les-Bois, France
- Phone: +33 774 43 5693
- Email: contact@notaire-saverys.fr
- Experience: 15+ years (since 2009)
- Core values: Rigueur, Disponibilité, Confiance
- Mission: "Votre partenaire juridique pour la vie"

## System Architecture

### Frontend Architecture
- **Template Engine**: Jinja2 templates with Flask
- **CSS Framework**: Bootstrap 5.3.0 for responsive design
- **Icons**: Font Awesome 6.4.0 for professional iconography
- **Fonts**: Google Fonts (Playfair Display and Source Sans Pro)
- **JavaScript**: Vanilla JavaScript for form validation and UI enhancements
- **Styling**: Custom CSS with French notary-appropriate color scheme (navy blue and gold)

### Backend Architecture
- **Framework**: Flask (Python) - lightweight web framework
- **Structure**: Simple MVC pattern with routes handling business logic
- **Email Service**: Flask-Mail for contact form submissions
- **Configuration**: Environment variables for sensitive data (email credentials, secret keys)
- **Logging**: Built-in Python logging configured for debugging

### Key Design Decisions
- **Server-side rendering**: Chosen for SEO optimization and simplicity, suitable for a professional service website
- **Static file structure**: CSS and JavaScript files served from static directory
- **French language**: All content in French to serve the target French clientele
- **Professional styling**: Navy and gold color scheme appropriate for legal services

## Key Components

### Routes and Pages
1. **Home (`/`)**: Hero section showcasing Maître Marc Saverys' expertise and service overview
2. **Services (`/services`)**: Detailed breakdown of notarial services (real estate, family law, succession, business law)
3. **About (`/about`)**: Attorney biography, credentials, and professional timeline for Maître Marc Saverys
4. **Contact (`/contact`)**: Contact form with email integration and office information

### Templates
- **Base template**: Shared layout with navigation, meta tags, and footer
- **Responsive navigation**: Bootstrap navbar with active state management
- **Service cards**: Reusable components for displaying service information
- **Contact form**: Multi-field form with validation and subject categorization

### Static Assets
- **Custom CSS**: Professional styling with CSS variables for consistent theming
- **JavaScript**: Form validation, smooth scrolling, and UI enhancements
- **Responsive design**: Mobile-first approach using Bootstrap grid system

## Data Flow

### Contact Form Processing
1. User submits contact form via POST to `/contact`
2. Flask validates required fields (name, email, subject, message)
3. Email is sent via Flask-Mail using configured SMTP settings
4. Success/error messages displayed via Flask's flash messaging
5. Form data is temporarily stored in request object (no persistent storage)

### Static Content Delivery
1. Template rendering combines base template with page-specific content
2. Static assets (CSS, JavaScript) served directly by Flask
3. External CDN resources loaded for Bootstrap and Font Awesome

## External Dependencies

### Python Packages
- **Flask**: Web framework and template engine
- **Flask-Mail**: Email functionality for contact forms

### Frontend Dependencies (CDN)
- **Bootstrap 5.3.0**: CSS framework for responsive design
- **Font Awesome 6.4.0**: Icon library for professional UI elements
- **Google Fonts**: Typography (Playfair Display, Source Sans Pro)

### Email Integration
- **SMTP Configuration**: Gmail SMTP (configurable via environment variables)
- **TLS Security**: Encrypted email transmission
- **Environment Variables**: Secure credential management

## Deployment Strategy

### Configuration Management
- **Environment Variables**: Used for sensitive data (email credentials, secret keys)
- **Development Mode**: Default configurations for local development
- **Production Ready**: Proper secret key and email configuration required

### File Structure
```
/
├── app.py (main Flask application)
├── main.py (application entry point)
├── templates/ (Jinja2 templates)
├── static/
│   ├── css/ (custom styles)
│   └── js/ (client-side scripts)
```

### Deployment Considerations
- **Static Files**: Flask serves static files in development; production deployment should use web server for static file serving
- **Email Configuration**: Requires valid SMTP credentials for contact form functionality
- **Security**: Session secret key must be set for production use
- **Logging**: Debug logging enabled; should be adjusted for production environment

### Missing Components for Full Deployment
- **Database**: No persistent data storage currently implemented
- **Admin Interface**: No backend administration panel
- **Content Management**: All content is hardcoded in templates
- **Analytics**: No visitor tracking or analytics integration
- **SSL/HTTPS**: Not configured in application layer