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


Quick start
================================================================================

The following code tries to get you started quickly with **non-lazy** loading.

.. code-block:: python

    from lml.plugin import PluginInfo, PluginManager


    @PluginInfo("cuisine", tags=["Portable Battery"])
    class Boost(object):
        def make(self, food=None, **keywords):
            print("I can cook %s for robots" % food)


    class CuisineManager(PluginManager):
        def __init__(self):
            PluginManager.__init__(self, "cuisine")

        def get_a_plugin(self, food_name=None, **keywords):
            return PluginManager.get_a_plugin(self, key=food_name, **keywords)


    if __name__ == '__main__':
        manager = CuisineManager()
        chef = manager.get_a_plugin("Portable Battery")
        chef.make()


At a glance, above code simply replaces the Factory pattern should you write
them without lml. What's not obvious is, that once you got hands-on with it,
you can start work on how to do **lazy** loading.



Documentation
----------------

.. toctree::
   :maxdepth: 2

   design
   tutorial
   lml_log
   api

Beyond the documentation above, here is a list of projects using lml:

#. `pyexcel <https://github.com/pyexcel/pyexcel>`_
#. `pyecharts <https://github.com/pyecharts/pyecharts>`_
#. `moban <https://github.com/moremoban/moban>`_

lml is available on these distributions:

#. `ARCH linux <https://aur.archlinux.org/packages/python-lml/>`_
#. `Conda forge <https://anaconda.org/conda-forge/lml>`_
#. `OpenSuse <https://build.opensuse.org/package/show/devel:languages:python/python-lml>`_
