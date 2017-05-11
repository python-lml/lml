Robot Chef built with lml: Part 2: Plugin Tutorial
================================================================================

In previous section, the main component of robotchef has been explained on
how to use lml to load plugins. Let us look at the plugin and see
how the plugin should be written.


Built-in plugin
-----------------

.. _builtin_plugin:

Remember this interaction::

    $ robotchef "Portable Battery"
    I can cook Portable Battery for robots

The response comes from a built-in plugin. Here is
`the code <https://github.com/chfw/lml/blob/master/examples/robotchef/robotchef/robot_cuisine/electricity.py>`_:

.. code-block:: python
   :linenos:

   from robotchef.plugin import Chef


   class Boost(Chef):

       def make(self, food=None, **keywords):
           print("I can cook %s for robots" % food)

class `Boost` was obtained via CuisineManager when user types 'Portable Battery'. And
the food parameter was passed to the instance of Boost. `make` method was called and it
prints 'I can cook Portable Battery for robots'.

It is a no stranger. class `Boost` inherits robotchef's plugin interface and overrides
the make method.

Till now, you have not seen lml yet. Let us look at robot_cuisine module's
`__init__.py <https://github.com/chfw/lml/blob/master/examples/robotchef/robotchef/robot_cuisine/__init__.py>`_:

.. code-block:: python
   :linenos:

   from lml.registry import PluginList


   PluginList(__name__).add_a_plugin(
       'cuisine',
       'electricity.Boost',
       tags=['Portable Battery']
   )

This is the place class `Boost` gets registered with lml.

Line 4 initializes an instance of `:class:lml.registry.PluginList`. `__name__` variable
refers to the module name, and in this case it equals 'robotchef.robot_cuisine'.

Line 5 tells lml it is 'cuisine' plugin. Using `:class:lml.registry.PluginList`, you can register any named plugins as long as you have corresponding plugin manager
implemented, like CuisineManager. Let us recall that CuisineMananger has initialized
as 'cuisine'.

What's more important is what you do not see here. To avoid heavy duty loading, in
other words, to achieve lazy loading as promised by **lml**, you shall follow
this design principle: **not to import any un-necessary modules in your plugin
module's __init__.py**.

.. code-block:: python
   :linenos:

   class CuisineManager(PluginManager):
       def __init__(self):
           PluginManager.__init__(self, "cuisine")


Line 6 tells the plugin class can be found at this relative path 'electricity.Boost'.
Together with line 4, an absolute import path
'robotchef.robot_cuisine.electricity.Boost'was formed behind the scenes.

Line 7 tell lml that here are the dictionary keys to look up class 'Boost'.

That's all you need to write a built-in plugin. Before I end this sub section, let me
emphasize that 'robotchef.robot_cuisine' was loaded by the call to `scan_plugins`
method, which we discussed in previous section. At the line 3 in `robotchef.__init__.py`
declared 'robotchef.robot_cuisine' as white listed package.


Standalone plugin
---------------------

robotchef can be expanded to understand more cuisine as shown in previous section.
After British cuisine was installed, robotchef starts 'frying Fish and Chips'. Let
us look at how to get it implemented.

First of all, the source code directory the plugin package should start with
'robotchef_'. For British Cuisine, it is named as 'robotchef_britishcuisine'.
The reason is that robotchef is scanning modules with 'robotchef_' as prefix.
You can elect your prefix however you need to make it consistent cross all
standalone plugins.

Secondly in the module's __init__.py, you would the plugin declaration code as
in the following. But nothing else.

.. code-block:: python
   :linenos:

   from lml.registry import PluginList


   PluginList(__name__).add_a_plugin(
       'cuisine',
       'fry.Fry',
       tags=['Fish and Chips']
   ).add_a_plugin(
       'cuisine',
       'bake.Bake',
       tags=['Cornish Scone', 'Jacket Potato']
   )

British cuisine plugin has two 'chef', one does fry and the other does bake.

Line 8 uses a chain function call to add another plugin. In theory, you can add
as many plugin class as you judge appropriate.

Line 12 shows that tags is a list and you can put as many as you can.

Let's try it now::

    $ robotchef "Jacket Potato"
    I can bake Jacket Potato

Here is the code in `bake.py <https://github.com/chfw/lml/blob/master/examples/robotchef_britishcuisine/robotchef_britishcuisine/bake.py>`_:

.. code-block:: python
   :linenos:

   from robotchef.plugin import Chef


   class Bake(Chef):

       def make(self, food=None):
           print("I can bake " + food)

Nothing is special about `fry.py <https://github.com/chfw/lml/blob/master/examples/robotchef_britishcuisine/robotchef_britishcuisine/fry.py>`_ either, so you can have a look at it by yourself.

Let me wrap up this section. All you will need to do, in order to make a standalone
plugin, is to provide a package installer(setup.py and other related package files) for a built-in plugin.

More standalone plugins
-------------------------

You are left to install robotchef_chinesecuisine and robotchef_cook yourself and
explore their functionalities.

How to ask robotchef to forget British cuisine?
------------------------------------------------

The management of standalone plugins are left in the hands of the user. To prevent
robotchef from finding British cuisine, you can use pip to uninstall it, like this::

    $ pip uninstall robotchef_britishcuisine

