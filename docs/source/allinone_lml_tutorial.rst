Robot Chef all in one package with lml
================================================================================

Let us go through robotchef_allinone_lml and see how the lml package can be used
to implement a conventional factory pattern, as we did in previous section.
This section demonstrates that the lml based plugins can be made to load
immediately and in a single package. And this sections helps you to understand
the next section where we will make the plugins to be loaded later.

Please navigate to
`lml/examples <https://github.com/chfw/lml/tree/master/examples>`_,
you would find robotchef_allinone_lml and its packages. Do the following::

    $ cd robotchef_allinone_lml
    $ python setup.py install

And then you could try::

    $ robotchef_allinone_lml "Fish and Chips"
    I can fry Fish and Chips
	
Lml plugins and plugin manager
-------------------------------

.. image:: _static/images/robotchef_allinone_lml.svg

plugin.py
++++++++++

`CuisineManager` inherits from :class:`~lml.plugin.PluginManager` class and
replaces the static registry `PLUGINS` and the modular function `get_a_plugin`.
Please note that `CuisineManager` declares that it is a manager for plugin_type named
**cuisine**. 


.. literalinclude:: ../../examples/robotchef_allinone_lml/robotchef_allinone_lml/plugin.py
   :language: python
   :lines: 7-17

Next, the :class:`~lml.plugin.PluginInfo` decorates all Chef's subclasses as
**cuisine** plugins and register the decorated classes with the manager class
for **cuisine**, `CuisineManager`. The food names become the tags which will
be used to look up the classes.

.. literalinclude:: ../../examples/robotchef_allinone_lml/robotchef_allinone_lml/plugin.py
   :language: python
   :lines: 1, 18-

Here is the :ref:`rb3-diff-rb0-plugin`.  

main.py
+++++++++

The main code has been updated to reflect the changes in plugin.py. `CuisineManager`
has to be instantiated to be the a factory manager.

.. literalinclude:: ../../examples/robotchef_allinone_lml/robotchef_allinone_lml/main.py
   :diff: ../../examples/robotchef_allinone/robotchef_allinone/main.py
