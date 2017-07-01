# -*- coding: utf-8 -*-
DESCRIPTION = (
    'Load me later. A lazy loading plugin management system.' +
    ''
)
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
	'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinxcontrib.spelling'
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'lml'
copyright = u'2017 Onni Software Ltd.'
version = '0.0.1'
release = '0.0.1'
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
spelling_lang = 'en_GB'
spelling_word_list_filename = 'spelling_wordlist.txt'
