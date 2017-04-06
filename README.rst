================================================================================
lml - Load me later. A lazy loading plugin management system.
================================================================================

.. image:: https://api.travis-ci.org/chfw/lml.svg?branch=master
   :target: http://travis-ci.org/chfw/lml

.. image:: https://codecov.io/github/chfw/lml/coverage.png
    :target: https://codecov.io/github/chfw/lml

.. image:: https://readthedocs.org/projects/lml/badge/?version=latest
   :target: http://lml.readthedocs.org/en/latest/

**lml** automatically load plugins that extend the main component from your
python environment, which could be your virtual environment, PyInstaller
environment. Its main feature is lazy loading. There could be hundreds of
plugins in your python environment but only a handful of plugins are loaded
when they are really needed. 

More documentation to follow.

Installation
================================================================================

You can install it via pip:

.. code-block:: bash

    $ pip install lml


or clone it and install it:

.. code-block:: bash

    $ git clone http://github.com/chfw/lml.git
    $ cd lml
    $ python setup.py install
