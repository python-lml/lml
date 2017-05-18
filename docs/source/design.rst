Design idea
=====================

The idea started with pyexcel project which uses loosely coupled plugins to extend
the capabilities of the main package. During its code growth, the code to load
the plugin later becomes a independent library, lml.

Prior to lml, three different ways of loading external plugins have been tried.
namespace package[#f1]_ comes from Python 3 or pkgutil style in Python 2 and 3.
It allows the developer to split a bigger packages into a smaller ones and
publish them separately. However, namespace package place strict requirements
on the module's __init__.py: nothing other than name space delaration should
be present. It means no module level functions can be place there. This restriction
destroy the individuality of the plugin. So namespace package was ruled out.

The Flask extension management system was used early versions of pyexcel(=<0.21).
This system manipulates sys.path so that your plugin package appears in the namespace
of your main package. For example, there is a xls plugin called pyexcel-xls. To
import it, you can use "import pyexcel.ext.xls". The shortcomings are:

#. explicit state "import pyexcel.ext.xls" becomes a useless statement in your code.
   static code ananlyzer(flake8/pep8/pycharm) would flag it up.
#. you have to explicitly import it. Otherwise, your plugin is not imported.

In order to overcome those shortcomings, implicit imports were coded into module's
__init__.py. By iterating through currently installed modules in your python
environment, the relevant plugins are imported automatically.

In terms of plugin registrations, three different approaches have been tried as
well. monkey-patching was first choice and was easy to implement. When a plugin
is imported, it load the plugin dictionary from the main package and add itself.
The registration code exists in plugin code.

another way of doing it is to place the plugin code in the main component and the
plugin just need to declare a dictionary as the plugin's meta data. The main package
register the meta data when it is imported.

The third way is to use meta-classes. A meta class can be used to register its
offsprings on its construction at program run time.

lml uses implicit import to load its plugins and combines meta data and meta class
for plugin registration. In terms of plugin distribution, like namespace packages and
flask extensions, lml plugins can be released to pypi and be installed by your end
developers.

Looking in the community, there are many plugin frameworks:

yapsy[#f2]_ is another simple plugin framework. It tries to emphasize on how simple
plugin interface could be designed. Yet it did not address the distribution of
the plugins, especially if a third party plugin, released to pypi, how can be
integrated easily.

GEdit plugin management system[#f3]_ load plugins from file system and show case
its plugin interfaces. The installation of its plugins is to do a manual
copy of the plugin to a desginated plugin directory.

lml is different from those two systems. It provides functionalities to
discover, register and load lml based plugins. It cares how the meta data were written
but it does care how the plugin interface is written.

To use lml, it asks you to avoid importing your "heavy" depdencies
in __init__.py. lml also respects the independency of individual packages. You can
put modular level functions in your __init__.py as long as it does not trigger
immediate import of your dependency. This is to allow the individual plugin to
become useful as it is, rather to be integrated with your main package. For example,
pyexcel-xls can be an independent package to read and write xls data, without pyexcel.

With lml, as long as your third party developer respect the plugin name prefix,
they could publish their plugins as they do to any normal pypi packages. And the end
developer of yours would only need to do pip install.

.. [#f1] https://packaging.python.org/namespace_packages/
.. [#f2] http://yapsy.sourceforge.net/
.. [#f3] https://wiki.gnome.org/Apps/Gedit/PythonPluginHowToOld
