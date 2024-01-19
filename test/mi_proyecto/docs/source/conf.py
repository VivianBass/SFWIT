# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
import django

sys.path.insert(0,os.path.abspath(".."))
os.environ['DJANGO_SETTINGS_MODULE'] = 'mi_proyecto.settings'
django.setup()

project = 'Mi aplicacion'
copyright = '2024, Equipo 4'
author = 'Equipo 4'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.todo","sphinx.ext.viewcode","sphinx.ext.autodoc"]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'es'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
# html_static_path = ['_static']
# html_favicon = '_static/favicon.ico'

# autodoc_mock_imports = [
#     'django',
#     'django.contrib.sessions.models',
#     'django.contrib.auth.models',
#     'django.db'
# ]