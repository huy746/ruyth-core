import os
import sys

# -- Path setup -----------------------------------------------------
sys.path.insert(0, os.path.abspath('../../'))

# -- Project information --------------------------------------------
project = 'ruythcore'
copyright = '2025, Huy'
author = 'ruythbot_huy'
release = '1.0.0'

# -- General configuration ------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output ----------------------------------------
html_theme = 'furo'  # đẹp hơn alabaster
html_static_path = ['_static']


