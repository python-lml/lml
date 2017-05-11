Use lml to write a shared library
===================================

In previous sections, lml was used write a scalble command line package. In this
section, I am going to explain how to use lml to write a shared api library.

Nagivate to `lml/examples/v2 <https://github.com/chfw/lml/tree/master/examples/v2>`_,
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
    $ robotchef "Jacket Potato"
    I do not know how to cook Jacket Potato


.. code-block:: python
   :linenos:


   from lml.loader import scan_plugins
   
   
   BUILTINS = ['robotchef.robot_cuisine']
   
   
   scan_plugins("robotchef_", __path__, white_list=BUILTINS)

