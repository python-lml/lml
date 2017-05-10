API tutorial
===============

.. code-block:: python
   :linenos:


   from lml.loader import scan_plugins
   
   
   BUILTINS = ['robotchef.robot_cuisine']
   
   
   scan_plugins("robotchef_", __path__, white_list=BUILTINS)

