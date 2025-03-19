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

**lml** effortlessly discovers lml-based plugins within your current Python
environment and loads them as needed. It is specifically designed to support
plugins with external dependencies, particularly those that are large or
memory-intensive. lml offers a plugin management system, while the plugin
interface remains your responsibility.

Applications that use lml benefit your customers in two key ways:

#. Customers can selectively install plugins from PyPI for each Python
   environment, and easily remove them using the pip uninstall command.
#. Only the plugins that are actively used at runtime are loaded into
   memory, optimizing resource usage.

When refactoring your existing code with lml, the goal is to simplify
complexity and reduce the size of your bulky Python library by distributing
related functionalities across plugins. However, the actual code refactoring
is up to you—the developer—while lml provides valuable support in the process.


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
