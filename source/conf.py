"""Sphinx configuration for the Python-OC-Lettings-FR documentation."""

import os
import sys
from pathlib import Path

# -- Path setup --------------------------------------------------------------
# Make the Django project importable so autodoc can pull in docstrings from
# models, views, etc. This documentation lives in its own repository,
# separate from the Django project. For LOCAL builds, we assume the two
# repositories are cloned side by side:
#   projet13/
#     docs/                       <- this repo
#     Python-OC-Lettings-FR/      <- the Django project
# On Read the Docs, this sibling checkout will NOT be present (only this
# docs repo is cloned), so autodoc will not find the modules there. In that
# case, install the project as a dependency in docs/requirements.txt
# (e.g. `git+https://github.com/<user>/Python-OC-Lettings-FR.git`) so it is
# importable from the build environment instead of relying on a sibling
# checkout.
DOCS_DIR = Path(__file__).resolve().parent
SIBLING_PROJECT_ROOT = DOCS_DIR.parent.parent / "Python-OC-Lettings-FR"
if SIBLING_PROJECT_ROOT.is_dir():
    sys.path.insert(0, str(SIBLING_PROJECT_ROOT))

# Minimal environment so Django can be configured without a real .env file
# (used both for local builds and on Read the Docs).
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oc_lettings_site.settings")
os.environ.setdefault("SECRET_KEY", "docs-build-secret-key")
os.environ.setdefault("ALLOWED_HOSTS", "localhost")

try:
    import django

    django.setup()
except Exception:  # noqa: BLE001 - autodoc must not crash the whole build
    pass

# -- Project information ------------------------------------------------------

project = "Python-OC-Lettings-FR"
copyright = "2026, Orange County Lettings"
author = "Orange County Lettings"
release = "0.1.0"

# -- General configuration ----------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "myst_parser",
    "sphinxcontrib.mermaid",
]

myst_enable_extensions = [
    "colon_fence",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

autodoc_default_options = {
    "members": True,
    "undoc-members": False,
    "show-inheritance": True,
}
autodoc_mock_imports = ["psycopg2"]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "django": (
        "https://docs.djangoproject.com/en/5.2/",
        "https://docs.djangoproject.com/en/5.2/_objects/",
    ),
}

# -- Options for HTML output ---------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_title = "Python-OC-Lettings-FR"
