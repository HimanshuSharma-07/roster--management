"""
WSGI config for roster_system project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roster_system.settings')

application = get_wsgi_application()

<<<<<<< HEAD:RosterApp/roster_system/wsgi.py
=======
<<<<<<< HEAD:roster_system/wsgi.py

app = application
=======
>>>>>>> 9779b07 (Add CSS styles and sample roster data):RosterApp/roster_system/wsgi.py
>>>>>>> 1e38777 (Add CSS styles and sample roster data):roster_system/wsgi.py
