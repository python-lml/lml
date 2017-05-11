# -*- coding: utf-8 -*-
DESCRIPTION = (
    'It understands world cuisine' +
    ''
)
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'robotchef_v2'
copyright = u'2017 Onni Software Ltd.'
version = '0.0.1'
release = '0.0.1'
exclude_patterns = []
pygments_style = 'sphinx'
html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'robotchef_v2doc'
latex_elements = {}
latex_documents = [
    ('index', 'robotchef_v2.tex',
     'robotchef_v2 Documentation',
     'Onni Software Ltd.', 'manual'),
]
man_pages = [
    ('index', 'robotchef_v2',
     'robotchef_v2 Documentation',
     [u'Onni Software Ltd.'], 1)
]
texinfo_documents = [
    ('index', 'robotchef_v2',
     'robotchef_v2 Documentation',
     'Onni Software Ltd.', 'robotchef_v2',
     DESCRIPTION,
     'Miscellaneous'),
]
