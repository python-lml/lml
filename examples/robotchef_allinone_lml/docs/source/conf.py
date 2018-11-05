# -*- coding: utf-8 -*-
DESCRIPTION = "it cook food" + ""
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
]

templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"

project = u"robotchef_allinone_lml"
copyright = u"2017 Onni Software Ltd."
version = "0.0.1"
release = "0.0.1"
exclude_patterns = []
pygments_style = "sphinx"
html_theme = "default"
html_static_path = ["_static"]
htmlhelp_basename = "robotchef_allinone_lmldoc"
latex_elements = {}
latex_documents = [
    (
        "index",
        "robotchef_allinone_lml.tex",
        "robotchef_allinone_lml Documentation",
        "Onni Software Ltd.",
        "manual",
    )
]
man_pages = [
    (
        "index",
        "robotchef_allinone_lml",
        "robotchef_allinone_lml Documentation",
        [u"Onni Software Ltd."],
        1,
    )
]
texinfo_documents = [
    (
        "index",
        "robotchef_allinone_lml",
        "robotchef_allinone_lml Documentation",
        "Onni Software Ltd.",
        "robotchef_allinone_lml",
        DESCRIPTION,
        "Miscellaneous",
    )
]
