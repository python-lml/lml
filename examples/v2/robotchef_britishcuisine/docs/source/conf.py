# -*- coding: utf-8 -*-
DESCRIPTION = "Cook food in british cuisine." + ""
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
]

templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"

project = u"robotchef_britishcuisine"
copyright = u"2017 Onni Software Ltd."
version = "0.0.1"
release = "0.0.1"
exclude_patterns = []
pygments_style = "sphinx"
html_theme = "default"
html_static_path = ["_static"]
htmlhelp_basename = "robotchef_britishcuisinedoc"
latex_elements = {}
latex_documents = [
    (
        "index",
        "robotchef_britishcuisine.tex",
        "robotchef_britishcuisine Documentation",
        "Onni Software Ltd.",
        "manual",
    )
]
man_pages = [
    (
        "index",
        "robotchef_britishcuisine",
        "robotchef_britishcuisine Documentation",
        [u"Onni Software Ltd."],
        1,
    )
]
texinfo_documents = [
    (
        "index",
        "robotchef_britishcuisine",
        "robotchef_britishcuisine Documentation",
        "Onni Software Ltd.",
        "robotchef_britishcuisine",
        DESCRIPTION,
        "Miscellaneous",
    )
]
