Robot Chef distributed in multiple packages: Part 1 main package
=================================================================

.. note::

   If you have skipped all in one Robot Chef section, you may want to do so::

       $ git clone https://github.com/chfw/lml.git


Let us have a look at a software component based approach to **Robot Chef**.
Navigate to `lml/examples <https://github.com/chfw/lml/tree/master/examples>`_,
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

The more cuisine packages you install, the more dishes it understands.


How lml was used to write up the robotchef
----------------------------------------------------------

.. image:: _static/images/loading_sequence.svg


Let us look at the main code(main.py) of robotchef. The code does these things:

#. scan for robotchef plugins
#. look up a chef and employ it to make the food

.. literalinclude:: ../../examples/robotchef/robotchef/main.py
   :language: python
   :linenos:

Line 8 lists 'robotchef.robot_cuisine' as the only one built-in plugin. It will return
a chef that cooks "Portable Battery".

What's extra here is line 16, where `:meth:lml.loader.scan_plugins` search through all
installed python modules and register plugin modules that has prefix "robotchef_".

At line 16, the second parameter of scan_plugins is to inform pyinstaller about the
package path if your package is to be packaged up. `white_list` lists the built-ins
packages.

Once scan_plugins is executed, all 'cuisine' plugins in your python path, including
the built-in ones will be discovered and will be collected in a dictionary for
`:meth:lml.PluginManager.get_a_plugin` to look up.

So let's read the code difference against lml version of Robot Chef, you will find that
except the plugin scanning code, both main.py are idential. The main functions in
a similar way as the all-in-one code: it takes the first argument
as food and pass it to an instance of CuisineManager, which returns a Chef that
"make" the food. NoChefException is raised when a chef is not found.


.. literalinclude:: ../../examples/robotchef/robotchef/main.py
   :diff: ../../examples/robotchef_allinone_lml/robotchef_allinone_lml/main.py


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
