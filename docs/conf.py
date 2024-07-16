import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'Sample Project'
author = 'Your Name'
release = '0.1.0'

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.ifconfig",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.imgmath",
    "sphinx.ext.viewcode",
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_sidebars = {
    "**": ["searchbox.html", "globaltoc.html", "sourcelink.html"],
}
html_static_path = ['_static']
