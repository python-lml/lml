Design idea
================================================================================

The idea, to load the plugins later, originated from pyexcel project [#f1]_ which uses
loosely coupled plugins to extend the main package to read more file formats. During
its code growth, the code in pyexcel packages to manage the external and internal
plugins becomes a independent library, lml.

lml is similar to **Factories** in
Zope Component Architecture [#f2]_. Lml provides functionalities to
discover, register and load lml based plugins. It cares how the meta data were
written but it does care how the plugin interface is written.


Plugin discovery
--------------------

Prior to lml, three different ways of loading external plugins have been tried in pyexcel.
namespace package [#f3]_ comes from Python 3 or pkgutil style in Python 2 and 3.
It allows the developer to split a bigger packages into a smaller ones and
publish them separately. sphinxcontrib [#f4]_ uses a typical namespace package based
method. However, namespace package places a strict requirement
on the module's __init__.py: nothing other than name space declaration should
be present. It means no module level functions can be place there. This restriction
forces the plugin to be driven by the main package but the plugin cannot use
the main package as its own library to do specific things. So namespace package
was ruled out.

The Flask extension management system was used early versions of pyexcel(=<0.21).
This system manipulates sys.path so that your plugin package appears in the namespace
of your main package. For example, there is a xls plugin called pyexcel-xls. To
import it, you can use "import pyexcel.ext.xls". The shortcomings are:

#. explicit statement "import pyexcel.ext.xls" becomes a useless statement in your code.
   static code analyser(flake8/pep8/pycharm) would flag it up.
#. you have to explicitly import it. Otherwise, your plugin is not imported.
   `PR 7 <https://github.com/pyexcel/pyexcel-io/pull/7>`_ of pyexcel-io has extended
   discussion on this topic.
#. flask extension management system become deprecated by itself in Flask's recent
   development since 2016.

In order to overcome those shortcomings, implicit imports were coded into module's
__init__.py. By iterating through currently installed modules in your python
environment, the relevant plugins are imported automatically.

lml uses implicit import. In order to manage the plugins, pip can be used to
install cherry-picked plugins or to remove unwanted plugins. In the situation
where two plugins perform the same thing but have to co-exist in your current
python path, you can nominate one plugin to be picked.

Plugin registration
---------------------

In terms of plugin registrations, three different approaches have been tried.
Monkey-patching was easy to implement. When a plugin is imported, it loads
the plugin dictionary from the main package and add itself.
But it is generally perceived as a "bad" idea.
Another way of doing it is to place
the plugin code in the main component and the plugin just need to declare a
dictionary as the plugin's meta data. The main package register the meta data
when it is imported. tablib [#f5]_ uses such a approach.
The third way is to use meta-classes. M. Alchin (2008) [#f6]_ explained how meta class can
be used to register plugin classes in a simpler way.

lml uses meta data for plugin registration. Since lml load your plugin later,
the meta data is stored in the module's __init__.py. For example, to load plugins later
in tablib, the 'exports' variable should be taken out from the actual class file and
replace the hard reference to the classes with class path string.

Plugin distribution
---------------------

In terms of plugin distribution, yapsy [#f7]_ and GEdit plugin management
system [#f8]_ load plugins from file system.
To install a plugin in those systems, is to copy and paste the plugin code to a
designated directory. zope components, namespace packages and flask extensions
can be installed via pypi. lml support the latter approach. lml plugins can be
released to pypi and be installed by your end developers.

Design principle
------------------

To use lml, it asks you to avoid importing your "heavy" dependencies
in __init__.py. lml also respects the independence of individual packages. You can
put modular level functions in your __init__.py as long as it does not trigger
immediate import of your dependency. This is to allow the individual plugin to
become useful as it is, rather to be integrated with your main package. For example,
pyexcel-xls can be an independent package to read and write xls data, without pyexcel.

With lml, as long as your third party developer respect the plugin name prefix,
they could publish their plugins as they do to any normal pypi packages. And the end
developer of yours would only need to do pip install.


References
-------------

.. [#f1] https://github.com/pyexcel/pyexcel
.. [#f2] http://zopecomponent.readthedocs.io/en/latest/
.. [#f3] https://packaging.python.org/namespace_packages/
.. [#f4] https://bitbucket.org/birkenfeld/sphinx-contrib/
.. [#f5] https://github.com/kennethreitz/tablib
.. [#f6] M. Alchin, 2008, A Simple Plugin Framework, http://martyalchin.com/2008/jan/10/simple-plugin-framework/
.. [#f7] http://yapsy.sourceforge.net/
.. [#f8] https://wiki.gnome.org/Apps/Gedit/PythonPluginHowToOld
