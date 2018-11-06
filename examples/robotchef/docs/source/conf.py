# -*- coding: utf-8 -*-
DESCRIPTION = "Sample project to demonstrate load me later plugin system" + ""
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
]

templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"

project = u"robotchef"
copyright = u"2017 Onni Software Ltd."
version = "0.0.1"
release = "0.0.1"
exclude_patterns = []
pygments_style = "sphinx"
html_theme = "default"
html_static_path = ["_static"]
htmlhelp_basename = "robotchefdoc"
latex_elements = {}
latex_documents = [
    (
        "index",
        "robotchef.tex",
        "robotchef Documentation",
        "Onni Software Ltd.",
        "manual",
    )
]
man_pages = [
    (
        "index",
        "robotchef",
        "robotchef Documentation",
        [u"Onni Software Ltd."],
        1,
    )
]
texinfo_documents = [
    (
        "index",
        "robotchef",
        "robotchef Documentation",
        "Onni Software Ltd.",
        "robotchef",
        DESCRIPTION,
        "Miscellaneous",
    )
]
