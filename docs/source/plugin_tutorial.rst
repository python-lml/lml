Plugin Tutorial
================================================================================

In previous section, the main component of robotchef has been explained on
how to use lml to load plugins. Let us look at the plugin and see
how the plugin should be written. 



Built-in plugin
-----------------

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
the make method. That is what you would write without lml. Where is class `Chef`?
Let's look at in `robotchef.plugin <https://github.com/chfw/lml/blob/master/examples/robotchef/robotchef/plugin.py>`_ :

.. code-block:: python
   :linenos:

   class Chef(object):
   
       def make(self, **params):
           print(self.name)

class `Chef` defines the plugin class interface. For robotchef, `make` is defined to
illustrate the functionality. Naturally you will be deciding the inteface for your
plugins.

Some of you might suggest that class `Chef` is unnecessary because Python uses
duck-typing, meaning as long as the plugin has `make` method, it should work. Yes,
it would work but it is a short term solution. Look at the long term, you could
pass on additional functionalities through class `Chef` without touching the
plugins. What's more, for plugin developers, a clear defined interface is better
than no class at all. And I believe the functions of a real plugin are more than
just one here.

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
implemeneted, like CuisineManager. Let us recall that CuisineMananger has initialized
as 'cuisine'.

What's more important is what you do not see here. To avoid heavy duty loading, in
other words, to achieve lazy loading as promised by **lml**, you are expected to
respect this principle: not to import any un-necessary modules in your plugin
module's __init__.py.

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
emphasize that 'robotchef.robot_cusisine' was loaded by the call to `scan_plugins`
method, which we discussed in previous section. At the line 3 in `robotchef.__init__.py`
declared 'robotchef.robot_cuisine' as white listed package.

.. code-block:: python
   :linenos:


   from lml.loader import scan_plugins
   
   
   BUILTINS = ['robotchef.robot_cuisine']
   
   
   scan_plugins("robotchef_", __path__, white_list=BUILTINS)

