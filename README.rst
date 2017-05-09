================================================================================
lml - Load me later. A lazy loading plugin management system.
================================================================================

.. image:: https://api.travis-ci.org/chfw/lml.svg?branch=master
   :target: http://travis-ci.org/chfw/lml

.. image:: https://codecov.io/github/chfw/lml/coverage.png
    :target: https://codecov.io/github/chfw/lml

.. image:: https://readthedocs.org/projects/lml/badge/?version=latest
   :target: http://lml.readthedocs.org/en/latest/

**lml** automatically loads plugins that extend the main component from your
current python environment. Its main feature is lazy loading. There could be
hundreds of plugins in your python environment. You may want to load
a handful of plugins when they are really needed. Or your plugins may
bring in a memory consuming dependency, so you may load it when necessary.

Installation
================================================================================

You can install it via pip:

.. code-block:: bash

    $ pip install lml


or clone it and install it:

.. code-block:: bash

    $ git clone https://github.com/chfw/lml.git
    $ cd lml
    $ python setup.py install
