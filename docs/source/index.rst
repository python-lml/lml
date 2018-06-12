`lml` - Load me later. A lazy plugin management system.
================================================================================


:Author: C.W.
:Source code: http://github.com/lml/lml.git
:Issues: http://github.com/lml/lml/issues
:License: New BSD License
:Released: |version|
:Generated: |today|


Introduction
-------------

**lml** seamlessly finds the lml based plugins from your current python
environment but loads your plugins on demand. It is designed to support
plugins that have external dependencies, especially bulky and/or
memory hungry ones. lml provides the plugin management system only and the
plugin interface is on your shoulder.

**lml** enabled applications helps your customers [#f1]_ in two ways:

#. Your customers could cherry-pick the plugins from pypi per python environment.
   They could remove a plugin using `pip uninstall` command.
#. Only the plugins used at runtime gets loaded into computer memory.

When you would use **lml** to refactor your existing code, it aims to flatten the
complexity and to shrink the size of your bulky python library by
distributing the similar functionalities across its plugins. However, you as
the developer need to do the code refactoring by yourself and lml would lend you a hand.

.. [#f1] the end developers who uses your library and packages achieve their
         objectives.


Documentation
----------------

.. toctree::
   :maxdepth: 2

   design
   tutorial
   lml_log
   api

Beyond the documentation above, here is a list of projects using lml:

#. `pyexcel <https://github.com/pyexcel.pyexcel>`_
#. `pyexcel-io <https://github.com/pyexcel.pyexcel-io>`_
#. `pyexcel-chart <https://github.com/pyexcel.pyexcel-chart>`_
