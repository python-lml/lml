# -*- coding: utf-8 -*-
DESCRIPTION = (
    'It does cooking' +
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

project = u'robotchef_allinone'
copyright = u'2017 Onni Software Ltd.'
version = '0.0.1'
release = '0.0.1'
exclude_patterns = []
pygments_style = 'sphinx'
html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'robotchef_allinonedoc'
latex_elements = {}
latex_documents = [
    ('index', 'robotchef_allinone.tex',
     'robotchef_allinone Documentation',
     'Onni Software Ltd.', 'manual'),
]
man_pages = [
    ('index', 'robotchef_allinone',
     'robotchef_allinone Documentation',
     [u'Onni Software Ltd.'], 1)
]
texinfo_documents = [
    ('index', 'robotchef_allinone',
     'robotchef_allinone Documentation',
     'Onni Software Ltd.', 'robotchef_allinone',
     DESCRIPTION,
     'Miscellaneous'),
]
