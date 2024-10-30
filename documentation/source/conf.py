# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
sys.path.insert(0, os.path.abspath('../../'))




project = 'fractallib'
copyright = '2024, LASSIOUED Badis'
author = 'LASSIOUED Badis'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Configuration to add README to the main doc
source_suffix = ['.rst', '.md']  # Allows .md files in Sphinx
master_doc = 'index'  # Tells Sphinx that index.rst is the root

autodoc_mock_imports = ['setup']

extensions = [
    'myst_parser',  # Supports Markdown files
    'sphinx.ext.autodoc',  # For docstring documentation
    'sphinx.ext.napoleon'  # Google and NumPy style docstrings
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
