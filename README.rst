================================================================================
lml - Load me later. A lazy loading plugin management system.
================================================================================

.. image:: https://api.travis-ci.org/chfw/lml.svg?branch=master
   :target: http://travis-ci.org/chfw/lml

.. image:: https://codecov.io/github/chfw/lml/coverage.png
    :target: https://codecov.io/github/chfw/lml

.. image:: https://readthedocs.org/projects/lml/badge/?version=latest
   :target: http://lml.readthedocs.org/en/latest/

**lml** seamlessly finds the lml based plugins from your current python
environment but loads your plugins on demand. It is designed to support
plugins that have external dependencies, especally when they are bulky.

**lml** enabled applications helps your developer in two ways:

#. Your developer could cherry-pick the plugins from pypi.
#. Only the plugins used at runtime enter into computer memory.

When you would use lml to refactor your exixsting code, it aims to flatten the
complexity and to shrink the size of your bulky python library by
distributing the similar functionalities across
its plugins. However, you as the developer need to do the code refactoring by
yourslef and lml would lend you a hand.

   

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
