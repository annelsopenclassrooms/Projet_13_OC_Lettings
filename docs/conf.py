# Configuration file for the Sphinx documentation builder.
import os
import sys

# -- Path setup --------------------------------------------------------------

# Add project root (where manage.py is) to sys.path
sys.path.insert(0, os.path.abspath('..'))

# -- Django setup ------------------------------------------------------------

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oc_lettings_site.settings")

import django
django.setup()
# -- Project information

project = 'OC Lettings'
#copyright = '2021, Graziella'
author = 'Anne Le Ster'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'