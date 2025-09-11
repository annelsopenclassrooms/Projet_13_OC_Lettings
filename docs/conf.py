# Configuration file for the Sphinx documentation builder.

import os
import sys
import django

# -- Path setup --------------------------------------------------------------

# Add project root to sys.path (adjust if docs/ is not directly under project root)
sys.path.insert(0, os.path.abspath('..'))

# Set the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oc_lettings_site.settings")
django.setup()

# -- Project information -----------------------------------------------------

project = 'OC Lettings'
copyright = '2025, Anne Le Ster'
author = 'Anne Le Ster'

# -- General configuration ---------------------------------------------------

# Sphinx extensions
extensions = [
    "sphinx.ext.autodoc",      # auto-generate docs from docstrings
    "sphinx.ext.napoleon",     # support Google/NumPy style docstrings
    "myst_parser",             # support Markdown files
    "sphinx.ext.viewcode",     # add links to source code
]

# Templates path
templates_path = ['_templates']

# Exclude build and system files
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# HTML theme
html_theme = "sphinx_rtd_theme"  # Read the Docs theme
html_static_path = ['_static']

# -- Napoleon settings -------------------------------------------------------

napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True

# -- Autodoc settings --------------------------------------------------------

autoclass_content = "class"
autodoc_member_order = "bysource"

# -- MyST Parser settings ---------------------------------------------------

myst_enable_extensions = [
    "colon_fence",  # enable ::: fenced blocks if needed
]
