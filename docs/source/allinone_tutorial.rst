Robot Chef all in one package without lml
============================================================

Please checkout lml::

    $ git clone https://github.com/chfw/lml.git

And navigate to `lml/examples <https://github.com/chfw/lml/tree/master/examples>`_,
you would find robotchef_allinone and its packages. Do the following::

    $ cd robotchef_allinone
    $ python setup.py install

And then you could try::

    $ robotchef_allinone "Fish and Chips"
    I can fry Fish and Chips


Conventional plugin and plugin factory
---------------------------------------

Robot Chef has `Chef` as plugin interface that makes food.
Boost, Bake and Fry are the actual implementations. Boost
are for "robots". Bake and Fry are for human.

.. image:: _static/images/robot_chef.svg

Here is the implementation details. The PLUGINS at line
29 is a dictionary that has food name as key and Chef
descendants as values. `get_a_plugin` method at line 37
returns a Chef or raises NoChefException.

.. literalinclude:: ../../examples/robotchef_allinone/robotchef_allinone/plugin.py
  :language: python
  :linenos:
  :emphasize-lines: 29, 37

Let us glimpse through the main code:

.. literalinclude:: ../../examples/robotchef_allinone/robotchef_allinone/main.py
  :language: python
  :linenos:

The code takes the first command option as food name and feeds it to the
factory method `get_a_plugin`, which returns a Chef to "make" the food.
If no chef was found, it prints the default string: I do not know.

That is all about the all in one **Robot Chef**.
