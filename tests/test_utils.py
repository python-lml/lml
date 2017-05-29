from lml.plugin import PluginManager
from nose.tools import eq_, raises
from lml.utils import json_dumps
from lml.utils import do_import


def test_json_dumps():

    class TestClass:
        pass

    adict = dict(test=TestClass)
    json_dumps(adict)


def test_do_import():
    import pyexcel_test
    pyexcel_test_package = do_import("pyexcel_test")
    eq_(pyexcel_test_package, pyexcel_test)


def test_do_import_2():
    import lml.plugin as plugin
    themodule = do_import("lml.plugin")
    eq_(plugin, themodule)


@raises(ImportError)
def test_do_import_error():
    do_import("non.exist")


def test_do_import_cls():
    from lml.utils import do_import_class
    manager = do_import_class("lml.plugin.PluginManager")
    eq_(manager, PluginManager)
