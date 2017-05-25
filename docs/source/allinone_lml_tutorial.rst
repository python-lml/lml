Robot Chef all in one package with lml
=============================================================

Hey, the show is not over yet. I've gotten **Robot Chef** version
3 with all plugins in one package built using lml. **lml** is
designed to load your plugins later but can also load your plugins now. This
section tries to demonstrate that conventional plugins can be written using
lml. Sometimes, you may want to mix conventional(load-me-now) ones and load-me-later ones.

Please navigate to `lml/examples <https://github.com/chfw/lml/tree/master/examples>`_,
you would find robotchef_allinone_lml and its packages. Do the following::

    $ cd robotchef_allinone_lml
    $ python setup.py install

And then you could try::

    $ robotchef_allinone_lml "Fish and Chips"
    I can fry Fish and Chips
	
Lml plugins and plugin manager
-------------------------------

Remember the plugin.py in Robot Chef, here is the :ref:`rb3-diff-rb0-plugin`. In order
to use lml, a custom :class:`~lml.plugin.PluginManager` class should be created to manage 'cuisine' plugins.
So `CuisineManager` replaces the static registry `PLUGINS` and the modular function `get_a_plugin`

.. literalinclude:: ../../examples/robotchef_allinone_lml/robotchef_allinone_lml/plugin.py
   :language: python
   :linenos:
   :emphasize-lines: 25,32,39

Line 25, 32 and 39 show that :class:`~lml.plugin.PluginInfo` becomes a decorator to
establish the relationship between the decorated class and `CuisineManager`.
					 
Here is the main code for Robot Chef version 3. CuisineManager is instantiated in the code and implements the factory method
to return a chef depending on the food name.
Looking at :ref:`rb3-diff-rb0-main`, the changes are natural as plugin factory has been rewritten in plugin.py. The newly
implemented classes should be imported. What's more, it reads similar to Robot Chef's main.py.

.. literalinclude:: ../../examples/robotchef_allinone_lml/robotchef_allinone_lml/main.py
   :language: python

			



