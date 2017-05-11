Logging facility
======================

During the development of lml package, the logging facility helps debugging a lot. Let
me show you how to enable the logs of lml.


Enable the logging
-------------------

Let us open robotchef's `main.py <https://github.com/chfw/lml/blob/master/examples/robotchef/robotchef/main.py>`_. Insert the highlighted codes.

.. code-block:: python
    :linenos:
    :emphasize-lines: 5-10
   
    import sys
    
    from robotchef.plugin import CuisineManager
    
    import logging
    import logging.config
    
    logging.basicConfig(
        format='%(name)s - %(levelname)s - %(message)s',
        level=logging.DEBUG)
    
    
    def main():
        if len(sys.argv) < 2:
            sys.exit(-1)
    
        manager = CuisineManager()
    ...
    
Then you will need to run the installation again::

    $ cd robotchef
    $ python setup.py install

Let us run the command again::
   
   $ robotchef "Jacket Potato"
    > lml.plugin - DEBUG - register cuisine
    > lml.plugin - DEBUG - load cached values robotchef_britishcuisine.fry.Fry
    > robotchef.plugin.CuisineManager - DEBUG - load me later: robotchef_britishcuisine
    > robotchef.plugin.CuisineManager - DEBUG - {"path": "robotchef_britishcuisine.fry.Fry", "name": "cuisine"}
    > lml.plugin - DEBUG - load cached values robotchef_britishcuisine.bake.Bake
    > robotchef.plugin.CuisineManager - DEBUG - load me later: robotchef_britishcuisine
    > robotchef.plugin.CuisineManager - DEBUG - {"path": "robotchef_britishcuisine.bake.Bake", "name": "cuisine"}
    > lml.plugin - DEBUG - load cached values robotchef.robot_cuisine.electricity.Boost
    > robotchef.plugin.CuisineManager - DEBUG - load me later: robotchef
    > robotchef.plugin.CuisineManager - DEBUG - {"path": "robotchef.robot_cuisine.electricity.Boost", "name": "cuisine"}
    > robotchef.plugin.CuisineManager - DEBUG - get a plugin
    > robotchef.plugin.CuisineManager - DEBUG - load me now:Jacket Potato
    > robotchef.plugin.CuisineManager - DEBUG - import robotchef_britishcuisine.bake.Bake
   I can bake Jacket Potato

Each "load me later" statement show the plugin packages that has been discovered.
Right after it, the log texts show the parameter lml has received. As you can read, it
discovered three Chef instances: robotchef_britishcuisine.fry.Fry,
robotchef_britishcuisine.bake.Bake and robotchef.robot_cuisine.electricity.Boost.
However, they are not imported yet.

When the robotchef try to look up a plugin, it logs "get a plugin". And it is actual
time when a plugin is imported. 

The mysterious log is "load cached values ... ". This is because scan_plugins are called
before CuisineManager is instantiated. In other words, without an instance of
CuisineManager, lml would cache the plugin info until the instantiation
happens.
