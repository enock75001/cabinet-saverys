#!/usr/bin/env python3
"""
Script de lancement pour le site notaire
Usage: python run.py
"""
import os
from app import app

if __name__ == '__main__':
    # Configuration pour le développement
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    
    print("🏛️ Démarrage du site notaire...")
    print(f"📍 Port: {port}")
    print(f"🔧 Debug: {debug}")
    print("🌐 Accès: http://localhost:5000")
    
    app.run(host='0.0.0.0', port=port, debug=debug)