Robot Chef version 2: Use lml to write a shared library
=============================================================

In previous sections, lml was used write a scalable command line package. In this
section, I am going to explain how to use lml to write a shared api library in the
context of Robot Chef.

Navigate to `lml/examples/v2 <https://github.com/chfw/lml/tree/master/examples/v2>`_,
you would find robotchef and its packages. Do the following::

    $ virtualenv --no-site-packages robotchefv2
    $ source robotchefv2/bin/activate
    $ cd robotchef_v2
    $ python setup.py install
    $ cd robotchef_api
    $ python setup.py install

And then you can type in and test the second version of Robot Chef::

    $ robotchef_v2 "Portable Battery"
    I can cook Portable Battery for robots
    $ robotchef_v2 "Jacket Potato"
    I do not know how to cook Jacket Potato

In order to add "Jacket Potato" in the know-how, you would need to install
robotchef_britishcuisine in this folder::

    $ cd robotchef_britishcuisine
    $ python setup.py install
    $ robotchef_v2 "Jacket Potato"
    I can bake Jacket Potato

Let us look at main code robotchef_v2:

.. code-block:: python
   :linenos:
   :emphasize-lines: 2, 9

   ...
   from robotchef_api import cuisine_manager


   def main():
       ...
       food_name = sys.argv[1]
       try:
           knowledged_chef = cuisine_manager.get_a_plugin(food_name)
           knowledged_chef.make(food=food_name)
       except Exception:
           print("I do not know how to cook " + food_name)

Comparing with previous version of Robot Chef, line 2 imports cuisine_manager,
an instance of CuisinManager from robotchef_api. No other changes in the main code.
And that is all in robotchef_v2.

Now let us look at robotchef_api. In the following director listing, the plugin.py
and robot_cuisine is exactly the same as the :ref:`plugin.py <plugin>`
and :ref:`robot_cuisine <builtin_plugin>` in robotchef::

    __init__.py    plugin.py       robot_cuisine

Notably, the plugin loader is put in the __init__.py:

.. code-block:: python
   :linenos:


   from lml.loader import scan_plugins


   BUILTINS = ['robotchef.robot_cuisine']


   scan_plugins("robotchef_", __path__, white_list=BUILTINS)

scan_plugins here load all modules that start with "robotchef_" and as well as
the modules in the white_list. And that is how you will write the main component as
a library.

Built-in plugin and Standalone plugin
--------------------------------------

You may have noticed that a copy of robotchef_britishcuisine is placed in v2 directory.
Why not using the same one above v2 directory? although they are almost identical,
there is minor difference. robotchef_britishcuisine in v2 directory depends on
robotchef_api but the other British cuisine package depends on robotchef. Hence, if you
look at the fry.py in v2 directory, you will notice a slight difference:

.. code-block:: python
   :linenos:
   :emphasize-lines: 1

   from robotchef_api.plugin import Chef
   
   
   class Fry(Chef):
   
       def make(self, food=None):
           print("I can fry " + food)

The package where the Chef was defined is different. So I would like to conclude that
there are no difference in writing built-in plugins nor standalone plugins. 
