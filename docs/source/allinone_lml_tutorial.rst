Robot Chef all in one package with lml
=============================================================

Let us re-write the Robot Chef all in one package using lml.

Please navigate to
`lml/examples <https://github.com/chfw/lml/tree/master/examples>`_,
you would find robotchef_allinone_lml and its packages. Do
the following::

    $ cd robotchef_allinone_lml
    $ python setup.py install

And then you could try::

    $ robotchef_allinone_lml "Fish and Chips"
    I can fry Fish and Chips
	
Lml plugins and plugin manager
-------------------------------

Here is the :ref:`rb3-diff-rb0-plugin`.  In order to use lml, a custom
:class:`~lml.plugin.PluginManager` class should be created to manage 'cuisine' plugins.
So `CuisineManager` replaces the static registry `PLUGINS` and
the modular function `get_a_plugin`. With lml, CuisineManager inherits `:class:lml.PluginManager`
which hides the dictionary lookup, and just needs tell PluginManager what is the key.


.. literalinclude:: ../../examples/robotchef_allinone_lml/robotchef_allinone_lml/plugin.py
   :language: python
   :linenos:

Line 6, CuisineManager declares that it is a manager for plugins that has then name
'cuisine'. You will see in the later section that the plugins all says it belongs
to 'cuisine'.


Line 13, class `Chef` defines the plugin class interface. For robotchef, `make` is
defined to illustrate the functionality. Naturally you will be deciding the
interface for your plugins.

Some of you might suggest that class `Chef` is unnecessary because
Python uses duck-typing, meaning as long as the plugin has `make` method,
it should work. Yes, it would work but it is a short term solution.
Look at the long term, you could pass on additional functionalities
through class `Chef` without touching the plugins. What's more, for
plugin developers, a clear defined interface is better than no class
at all. And I believe the functions of a real plugin are more than
just one here.

:class:`~lml.plugin.PluginInfo` as a decorator
establishes the relationship between the decorated class and `CuisineManager`.
					 
Here is the main code for the re-written Robot Chef. CuisineManager is instantiated
in the code and implements the factory method to return a chef depending on the food name.
Looking at :ref:`rb3-diff-rb0-main`, the changes are natural as plugin factory
has been rewritten in plugin.py. The newly implemented classes should be imported.
What's more, it reads similar to Robot Chef's main.py.

.. literalinclude:: ../../examples/robotchef_allinone_lml/robotchef_allinone_lml/main.py
   :language: python

			



