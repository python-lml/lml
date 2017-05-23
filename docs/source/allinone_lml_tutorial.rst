Robot Chef version 3: All-in-one with lml
=============================================================

Hey, the show is not over yet. I've gotten **Robot Chef** version
3 with all plugins in one package built using lml. **lml** is
designed to load your plugins later but can also load your plugins now.

Please navigate to `lml/examples <https://github.com/chfw/lml/tree/master/examples>`_,
you would find robotchef_allinone_lml and its packages. Do the following::

    $ cd robotchef_allinone_lml
    $ python setup.py install

And then you could try::

    $ robotchef_allinone_lml "Fish and Chips"
    I can fry Fish and Chips

.. literalinclude:: ../../examples/robotchef_allinone_lml/robotchef_allinone_lml/main.py
   :diff: ../../examples/robotchef/robotchef/main.py
   :language: python




