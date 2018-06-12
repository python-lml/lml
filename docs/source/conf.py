# -*- coding: utf-8 -*-
DESCRIPTION = (
    'Load me later. A loading plugin management system.' +
    ''
)
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinxcontrib.spelling'
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'lml'
copyright = u'2017 Onni Software Ltd.'
version = '0.0.2'
release = '0.0.3'
exclude_patterns = []
pygments_style = 'sphinx'
html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'lmldoc'
latex_elements = {}
latex_documents = [
    ('index', 'lml.tex',
     'lml Documentation',
     'Onni Software Ltd.', 'manual'),
]
man_pages = [
    ('index', 'lml',
     'lml Documentation',
     [u'Onni Software Ltd.'], 1)
]
texinfo_documents = [
    ('index', 'lml',
     'lml Documentation',
     'Onni Software Ltd.', 'lml',
     DESCRIPTION,
     'Miscellaneous'),
]
