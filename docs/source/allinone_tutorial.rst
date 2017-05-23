Robot Chef in one package without lml
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

Let us glimpse through the main code:

.. literalinclude:: ../../examples/robotchef_allinone/robotchef_allinone/main.py
  :language: python
  :linenos:

The code takes the first command option as food name and feeds it to the
factory method `get_a_plugin`, which returns a Chef to "make" the food.
If no chef was found, it prints the default string: I do not know.

.. image:: _static/images/robot_chef.svg

Now let us move to plugin.py. Some of non-relevant lines were omitted here.

.. literalinclude:: ../../examples/robotchef_allinone/robotchef_allinone/plugin.py
  :language: python
  :linenos:

The PLUGINS is a dictionary that has food name as key and Chef descendants
as values. `get_a_plugin` method returns a Chef or raises NoChefException.

That is all about the all in one **Robot Chef**.
