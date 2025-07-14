import os
import sys
from django.core.wsgi import get_wsgi_application

# Add the project directory to the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vercel_deploy.settings')

application = get_wsgi_application()

# For Vercel compatibility
app = application