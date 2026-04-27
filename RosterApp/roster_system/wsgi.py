import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roster_system.settings')

application = get_wsgi_application()

# Alias for deployment platforms that expect 'app'
app = application
