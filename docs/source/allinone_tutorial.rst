Robot Chef in one package
============================

Please checkout lml::

    $ git clone https://github.com/chfw/lml.git

And nagivate to `lml/examples <https://github.com/chfw/lml/tree/master/examples>`_,
you would find robotchef_allinone and its packages. Do the following::

    $ cd robotchef_allinone
    $ python setup.py install

And then you could try::

    $ robotchef_allinone "Fish and Chips"
    I can fry Fish and Chips

Simple, isn't it? Let us glimpse through the main code:

.. code-block:: python
  :linenos:

  import sys

  import robotchef_allinone.plugin as cuisine_manager


  def main():
      if len(sys.argv) < 2:
          sys.exit(-1)

      food_name = sys.argv[1]
      try:
          knowledged_chef = cuisine_manager.get_a_plugin(food_name)
          knowledged_chef.make(food=food_name)
      except cuisine_manager.NoChefException:
          print("I do not know how to cook " + food_name)

The code takes the first command option as food name and feeds it to the
factory method `get_a_plugin`, which returns a Chef to "make" the food.
If no chef was found, it prints the default string: I do not know.

Now let us move to plugin.py. Some of non-relevant lines were omitted here.

.. code-block:: python
   :linenos:

   class NoChefException(Exception):
   ...

   class Chef(object):
   ...

   class Boost(Chef):
   
       def make(self, food=None, **keywords):
           print("I can cook %s for robots" % food)


   class Fry(Chef):

       def make(self, food=None):
           print("I can fry " + food)


   class Bake(Chef):
   ...

   PLUGINS = {
       "Portable Battery": Boost,
       "Fish and Chips": Fry,
       "Cornish Scone": Bake,
       "Jacket Potato": Bake
   }


   def get_a_plugin(food_name=None, **keywords):
       plugin = PLUGINS.get(food_name)
       if plugin is None:
           raise NoChefException("Cannot find a chef")
       plugin_cls = plugin()
       return plugin_cls

The PLUGINS is a dictionary that has food name as key and Chef descedents
as values. `get_a_plugin` method returns a Chef or raises NoChefException.

That is all about the all in one **Robot Chef**.

