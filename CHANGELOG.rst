Change log
================================================================================

0.2.0 - 16/03/2025
--------------------------------------------------------------------------------

**Updated**

#. replace __import__ with importlib

**Removed**

#. removed python 2 support

0.1.0 - 21/10/2020
--------------------------------------------------------------------------------

**Updated**

#. non class object can be a plugin too
#. `#20 <https://github.com/python-lml/lml/issues/20>`_: When a plugin was not
   installed, it now calls raise_exception method

0.0.9 - 7/1/2019
--------------------------------------------------------------------------------

**Updated**

#. `#11 <https://github.com/python-lml/lml/issues/11>`_: more test contents for
   OpenSuse package validation

0.0.8 - 4/1/2019
--------------------------------------------------------------------------------

**Updated**

#. `#9 <https://github.com/python-lml/lml/issues/9>`_: include tests, docs for
   OpenSuse package validation

0.0.7 - 17/11/2018
--------------------------------------------------------------------------------

**Fixed**

#. `#8 <https://github.com/python-lml/lml/issues/8>`_: get_primary_key will fail
   when a module is loaded later
#. deprecated old style plugin scanner: scan_plugins

0.0.6 - 07/11/2018
--------------------------------------------------------------------------------

**Fixed**

#. Revert the version 0.0.5 changes. Raise Import error and log the exception

0.0.5 - 06/11/2018
--------------------------------------------------------------------------------

**Fixed**

#. `#6 <https://github.com/python-lml/lml/issues/6>`_: Catch and Ignore
   ModuleNotFoundError

0.0.4 - 07.08.2018
--------------------------------------------------------------------------------

**Added**

#. `#4 <https://github.com/python-lml/lml/issues/4>`_: to find plugin names with
   different naming patterns

0.0.3 - 12/06/2018
--------------------------------------------------------------------------------

**Added**

#. `dict` can be a pluggable type in addition to `function`, `class`
#. get primary tag of your tag, helping you find out which category of plugins
   your tag points to

0.0.2 - 23/10/2017
--------------------------------------------------------------------------------

**Updated**

#. `pyexcel#103 <https://github.com/pyexcel/pyexcel/issues/103>`_: include
   LICENSE in tar ball

0.0.1 - 30/05/2017
--------------------------------------------------------------------------------

**Added**

#. First release
