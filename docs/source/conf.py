# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

sys.path.insert(0, os.path.abspath("_ext"))

project = 'UHDT-Sim'
copyright = '2026, Jia Jun Li, Connor Nishimoto, Tristan Ta'
author = 'Jia Jun Li, Connor Nishimoto, Tristan Ta'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx_favicon",
    "sphinx_design",
    "page_metadata",
]

myst_enable_extensions = [
    "colon_fence",
]

templates_path = ['_templates']
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'shibuya'
html_static_path = ['_static']

html_theme_options = {
    "light_logo": "_static/logo_light.png",
    "dark_logo": "_static/logo_dark.png",
    "accent_color": "blue",
}

html_favicon = "_static/Drone.png"