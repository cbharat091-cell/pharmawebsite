import os
import sys
import shutil

# Add the project directory to the Python path
project_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, project_dir)

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'final_pro.settings')

# Import Django and setup
import django
django.setup()

# Copy DB to /tmp if on Vercel
if 'VERCEL' in os.environ:
    db_path = os.path.join(project_dir, 'db.sqlite3')
    tmp_db = '/tmp/db.sqlite3'
    if os.path.exists(db_path) and not os.path.exists(tmp_db):
        shutil.copy(db_path, tmp_db)

# Import the WSGI application
from final_pro.wsgi import application

# For Vercel, we need to export the app
app = application
