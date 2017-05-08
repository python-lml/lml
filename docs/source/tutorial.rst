Tutorial
================================================================================

Let us have a look at a software component based command line application, called
**robot chef**. It does simply this::

    $ robotchef "Portal Battery"
    I can cook Portable Battery for robots

Although it does not understand all the cuisines in the world as you see
as below::

    $ robotchef "Fish and Chips"
    I do not know how to cook Fish and Chips

it starts to understand it once you install British cuisine package to complement
its knowledge. The more cuisine package you install, the more dishes it
understands.

Installing the robot chef and its British cuisine library
----------------------------------------------------------

Please checkout lml::

    $ git clone https://github.com/chfw/lml.git

And nagivate to `lml/examples <https://github.com/chfw/lml/tree/master/examples>`_,
you would find robotchef and its packages. Do the following::

    $ cd robotchef
    $ python setup.py install

And then please try the commands in the introduction. Having done that, could you
please try install robotchef_britishcuisine to your python environment::

    $ cd robotchef_britishcuisine
    $ python setup.py install

And then type in the following::

     $ robotchef "Fish and Chips"
     I can fry Fish and Chips

You would notice it replies positively.


.. note::

   To help you understand the internals of lml, the log were left on. We will
   come back to the log in the end.


How lml was used to write up the robotchef
----------------------------------------------------------

Let us look at the main code(main.py) of robotchef:

.. code-block:: python
   :linenos:


   from robotchef.plugin import CuisineManager


   def main():
      if len(sys.argv) < 2:
          sys.exit(-1)
   
      manager = CuisineManager()
      food_name = sys.argv[1]
      try:
          knowledged_chef = manager.get_a_plugin(food_name)
          print(knowledged_chef.make(food=food_name))
      except Exception:
          print("I do not know how to cook " + food_name)


CuisineManager is instantiated in the code and implements the factory method
to return a chef depending on the food name. The returned chef then make
the food. Otherwise, robotchef says "I do not know how to cook" the food. That
is pretty much what you would write without lml.

Now let us visit plugin.py to examine CuisineManger:

.. code-block:: python
   :linenos:

   from lml.plugin import PluginManager
   
   
   class CuisineManager(PluginManager):
       def __init__(self):
           PluginManager.__init__(self, "cuisine")
   
       def get_a_plugin(self, food_name=None, **keywords):
           return PluginManager.get_a_plugin(self, key=food_name, **keywords)


Line 8 shows the factory method that looks up a food name for plugin. In the
conventional construction method, I meant without thinking of loosely coupled
software components, you would expected to see a dictionary in `get_a_plugin`
method. `food_name` is the key and the return value would be the class that
understands the food. With lml, CuisineManager inherits `:class:lml.PluginManager`
which hides the dicionary lookup, and just needs tell PluginManager what is the
key.

Line 6, 'cuisine' play a significant role in the lml system. It becomes
the plugin name and you will see in the later section that the plugins shall
declare it is a plugin of 'cuisine'.

Are you with still with me so far? I have explained how a custom plugin manager
is used and how to inherit from `:class:lml.PluginManager`. If you would like
to get started with lml, these are pretty much the code you need to write in
your main component. Is that all? No, I have yet one more file to explain and
it is __init__.py file, where the plugins were discovered:


.. code-block:: python
   :linenos:


   from lml.loader import scan_plugins
   
   
   BUILTINS = ['robotchef.robot_cuisine']
   
   
   scan_plugins("robotchef_", __path__, white_list=BUILTINS)

 
Three lines of code here. scan_plugins would look up the installed modules that starts
with the prefix 'robotchef_'. The second parameter is to inform pyinstall about the
package path if your package is to be packaged up. `white_list` lists the built-ins
packages. 'robotchef.robot_cuisine' is the only bulit-in cusine plugin.

Once scan_plugins is executed, all 'cuisine' plugins in your python path, inlucding
the built-in ones will be discovered and will be collected in a dictionary for
`:meth:lml.PluginManager.get_a_plugin` to look up.

