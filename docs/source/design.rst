Design idea
=====================

It all started with pyexcel project which uses loosely coupled plugins to extend
the capabilities of the main package. During its code growth, the idea to load
the library later comes into formation.

In Python, there are more than one way to load plugins than lml. namespace package[#f1]
comes from Python 3 or pkgutil style in Python 2 and 3. It allows the developer
to split a bigger packages into a smaller ones and publish them separately. However,
namespace packages place strict requirements on the module's __init__.py: nothing
other than name space delaration should be present. However, lml only discourage
you from importing your "heavy" depdencies in __init__.py. lml also respects
the independency of individual packages. You can put modular level functions in your
__init__.py as long as it does not trigger immediate import of your dependency.

yapsy[#f2] is another simple plugin framework. It tries to emphasize on how simple
plugin interface could be designed. Yet it did not address the distribution of
the plugins, especially if a third party plugin, released to pypi, can be integrated
easily. With lml, as long as your third party developer respect the plugin name prefix,
they could publish their plugins as they do to any normal pypi packages. And the end
developer of yours would only need to do pip install.

GEdit plugin management system[#f3] load plugins from file system and show case
its plugin interfaces. The installation of its plugins is to do a manual
copy of the plugin to a desginated plugin directory. There is nothing wrong with it.
But lml tries to take adavantage of pypi and pip.


.. [#f1] https://packaging.python.org/namespace_packages/
.. [#f2] http://yapsy.sourceforge.net/
.. [#f3] https://wiki.gnome.org/Apps/Gedit/PythonPluginHowToOld
