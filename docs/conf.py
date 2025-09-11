import os
import sys
import django

# Chemin absolu vers la racine du projet (où se trouve manage.py)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

# Configuration Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oc_lettings_site.settings")
django.setup()

# -- Project information -----------------------------------------------------
project = 'OC Lettings Site'
copyright = '2025, Anne LS'
author = 'Anne LS'
release = '1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
