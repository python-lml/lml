Robot Chef built with lml: Part 1
====================================

.. note::

   If you have skipped all in one Robot Chef section, you may want to do so::

       $ git clone https://github.com/chfw/lml.git


Let us have a look at a software component based approach to **Robot Chef**.
Nagivate to `lml/examples <https://github.com/chfw/lml/tree/master/examples>`_,
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

Let us look at the main code(main.py) of robotchef. The code does these things:

#. scan for robotchef plugins
#. look up a chef and employ it to make the food

.. code-block:: python
   :linenos:
   :emphasize-lines: 6,11-12

   from lml.loader import scan_plugins

   from robotchef.plugin import CuisineManager, NoChefException


   BUILTINS = ['robotchef.robot_cuisine']


   def main():
       ...
       cuisine_manager = CuisineManager()
       scan_plugins("robotchef_", 'robotchef', white_list=BUILTINS)

       food_name = sys.argv[1]
       try:
           knowledged_chef = cuisine_manager.get_a_plugin(food_name)
           knowledged_chef.make(food=food_name)
       except NoChefException:
           print("I do not know how to cook " + food_name)


The main functions in a similiar way as the all-in-one code: it takes the first argument
as food and pass it to an instance of CuisineManager, which returns a Chef that
"make" the food. NoChefException is raised when a chef is not found.

Line 6 lists 'robotchef.robot_cuisine' as the only one built-in plugin. It will return
a chef that cooks "Portable Battery".

At line 11, CuisineManager is instantiated in the code and implements the factory method
to return a chef depending on the food name. 

What's extra here is line 12, where `:meth:lml.loader.scan_plugins` search through all
installed python modules and register plugin modules that has prefix "robotchef_".

At line 12, the second parameter of scan_plugins is to inform pyinstaller about the
package path if your package is to be packaged up. `white_list` lists the built-ins
packages.

Once scan_plugins is executed, all 'cuisine' plugins in your python path, including
the built-in ones will be discovered and will be collected in a dictionary for
`:meth:lml.PluginManager.get_a_plugin` to look up.

Plugin management
-----------------------

.. _plugin:


Now let us visit plugin.py to examine CuisineManger:

.. code-block:: python
   :linenos:

   from lml.plugin import PluginManager


   class CuisineManager(PluginManager):
       def __init__(self):
           PluginManager.__init__(self, "cuisine")

       def get_a_plugin(self, food_name=None, **keywords):
           return PluginManager.get_a_plugin(self, key=food_name, **keywords)

       def raise_exception(self, key):
           raise NoChefException("Cannot find a chef")
   
   
   class Chef(object):
   
       def make(self, **params):
           print("I am a chef")

Line 8 shows the factory method that looks up a food name for plugin. In the
conventional construction method, I meant without thinking of loosely coupled
software components, you would expected to see a dictionary in `get_a_plugin`
method. `food_name` is the key and the return value would be the class that
understands the food. With lml, CuisineManager inherits `:class:lml.PluginManager`
which hides the dicionary lookup, and just needs tell PluginManager what is the
key.

Line 6, CuisineManager declars that it is a manager for plugins that has then name
'cuisine'. You will see in the later section that the plugins all says it belongs
to 'cuisine'.

Line 13, class `Chef` defines the plugin class interface. For robotchef, `make` is
defined to illustrate the functionality. Naturally you will be deciding the
inteface for your plugins.

Some of you might suggest that class `Chef` is unnecessary because Python uses
duck-typing, meaning as long as the plugin has `make` method, it should work. Yes,
it would work but it is a short term solution. Look at the long term, you could
pass on additional functionalities through class `Chef` without touching the
plugins. What's more, for plugin developers, a clear defined interface is better
than no class at all. And I believe the functions of a real plugin are more than
just one here.

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
