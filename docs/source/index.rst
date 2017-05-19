`lml` - Load me later. A lazy loading plugin management system.
================================================================================


.. note::

   It is still under writing
 

:Author: C.W.
:Source code: http://github.com/lml/lml.git
:Issues: http://github.com/lml/lml/issues
:License: New BSD License
:Development: |release|
:Released: |version|
:Generated: |today|


Introduction
-------------

**lml** seamlessly finds the lml based plugins from your current python
environment but loads your plugins on demand. It is designed to support
plugins that have external dependencies, especially when they are bulky. lml
provides the plugin management system only and the plugin interface is on your
shoulder, my dear developer. 

**lml** enabled applications helps your developer in two ways:

#. Your developer could cherry-pick the plugins from pypi.
#. Only the plugins used at runtime enter into computer memory.

When you would use lml to refactor your existing code, it aims to flatten the
complexity and to shrink the size of your bulky python library by
distributing the similar functionalities across
its plugins. However, you as the developer need to do the code refactoring by
yourself and lml would lend you a hand.



Documentation
----------------

.. toctree::

   design
   tutorial
   api
