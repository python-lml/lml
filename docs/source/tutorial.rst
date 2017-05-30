Tutorial
================================================================================

In this tutorial, we are going to go through various ways to build
the command line application: **Robot Chef**. One is to build it as a single
package. Another is to build it using lml: one main component
with many plugins which are separately installable. By comparing the
different approaches to build Robot Chef, we could see how lml can be used
in practice.

**Robot Chef** would report what it knows about the food in the world. For
example::

    $ robotchef "Portable Battery"
    I can cook Portable Battery for robots

When you type "Fish and Chips", it could reports it does not know::

    $ robotchef "Fish and Chips"
    I do not know how to cook Fish and Chips

For it to understand all the cuisines in the world, there are two ways to
enlarge its knowledge base: one is obviously to grow by itself. the other
is to open the api interface so that others could join your effort.

.. toctree::

   allinone_tutorial
   allinone_lml_tutorial
   lml_tutorial
   api_tutorial

Additional references
----------------------

#. pyexcel-chart: `use lml to refactor existing plugins <https://github.com/pyexcel/pyexcel-chart/commit/ca307f49b10f00cd080a3321490acc7b89ca0a41>`_
