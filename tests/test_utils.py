from lml.utils import do_import, json_dumps
from lml.plugin import PluginManager

from unittest.mock import patch
from pytest import raises


def test_json_dumps():
    class TestClass:
        pass

    float_value = 1.3
    adict = dict(test=TestClass, normal=float_value)
    json_dumps(adict)


def test_do_import():
    import isort

    test_package = do_import("isort")
    assert test_package == isort


def test_do_import_2():
    import lml.plugin as plugin

    themodule = do_import("lml.plugin")
    assert plugin == themodule


@patch("lml.utils.log.exception")
def test_do_import_error(mock_exception):
    with raises(ImportError):
        do_import("non.exist")
    mock_exception.assert_called_with(
        "%s is absent or cannot be imported", "non.exist"
    )


def test_do_import_cls():
    from lml.utils import do_import_class

    manager = do_import_class("lml.plugin.PluginManager")
    assert manager == PluginManager
