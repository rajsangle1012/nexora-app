import os
import sys

# Add the backend directory to sys.path so we can import the Django project
backend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Nexora_backend'))
if backend_path not in sys.path:
    sys.path.append(backend_path)

from django.core.wsgi import get_wsgi_application

# Set the settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexora.settings")

# Get the WSGI application
app = get_wsgi_application()
