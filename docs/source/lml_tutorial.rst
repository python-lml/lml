Robot Chef distributed in multiple packages: Part 1 main package
================================================================================

In previous section, **Robot Chef** was written using lml but in a single
package and its plugins are loaded immediately. In this section, we will
decouple the plugin and the main package using lml. In Part 2, we will
demonstrates the changes needed to plugin them back with the main package.

Demo
--------------------------------------------------------------------------------

Please navigate to
`lml/examples <https://github.com/chfw/lml/tree/master/examples>`_,
you would find robotchef and its packages. Do the following::

    $ cd robotchef
    $ python setup.py install

The main command line interface module does simply this::

    $ robotchef "Portable Battery"
    I can cook Portable Battery for robots

Although it does not understand all the cuisines in the world as you see
as below::

    $ robotchef "Jacket Potato"
    I do not know how to cook Jacket Potato

it starts to understand it once you install Chinese cuisine package to complement
its knowledge::

    $ cd robotchef_britishcuisine
    $ python setup.py install

And then type in the following::

     $ robotchef "Fish and Chips"
     I can fry Fish and Chips

The more cuisine packages you install, the more dishes it understands. Here
is the loading sequence:

.. image:: _static/images/loading_sequence.svg


Decoupling the plugins with the main package
--------------------------------------------------------------------------------

.. image:: _static/images/robotchef_crd.svg


In order to demonstrate the capabilities of lml, `Boost` class is singled out and
placed into an internal module **robotchef.robot_cuisine**. `Fry` and `Bake` are
relocated to **robotchef_britishcuisine** package, which is separately installable.

After the separation, in order to piece all togother, a special function
:meth:`lml.loader.scan_plugins` needs to be called before the plugins are used.

.. literalinclude:: ../../examples/robotchef/robotchef/main.py
   :diff: ../../examples/robotchef_allinone_lml/robotchef_allinone_lml/main.py

What's more, `:meth:lml.loader.scan_plugins` search through all
installed python modules and register plugin modules that has prefix "robotchef_".

The second parameter of scan_plugins is to inform pyinstaller about the
package path if your package is to be packaged up using pyinstaller.
`white_list` lists the built-ins  packages.

Once scan_plugins is executed, all 'cuisine' plugins in your python path, including
the built-in ones will be discovered and will be collected by
:class:`~lml.plugin.PluginInfoChain` in a dictionary for
:meth:`~lml.PluginManager.get_a_plugin` to look up.


Plugin management
-----------------------

.. _plugin:


Now let us visit plugin.py to examine CuisineManger:

.. literalinclude:: ../../examples/robotchef/robotchef/plugin.py
  :language: python
  :linenos:

Are you with still with me so far? I have explained how a custom plugin manager
is used and how to inherit from `:class:lml.PluginManager`. If you would like
to get started with lml, these are pretty much the code you need to write in
your main component. Is that all? No, I have yet one more file to explain and
it is __init__.py file, where the plugins were discovered:


That is all you need to make your main component to start using component based approach
to expand its functionalities. Here is the takeaway for you:

#. `:class:lml.PluginManager` is just another factory pattern that hides the
   complexity away.
#. You will need to call `:meth:lml.scan_plugins` in your __init__.py or where
   appropriate but make sure it is called.

