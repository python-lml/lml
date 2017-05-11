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

**lml** automatically but lazily loads plugins for your application from
current python environment. It aims to flatten the complexity and to shrink the
size of your bulky python library by distributing the similar functionalities across
its plugins. However, you as the developer need to do the code refactoring by
yourself and lml would lend you a hand.

**lml** enabled applications helps your developer in two ways:

#. There could be hundreds of plugins on pypi. Your developer could cherry-pick the
plugins they would use
#. There could be many plugins installed in your developer's python environment.
Only the plugins used at runtime enter into computer memory.


Documentation
----------------

.. toctree::

   design
   tutorial
   api
