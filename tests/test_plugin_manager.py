from mock import patch
from lml.plugin import PluginManager, PLUG_IN_MANAGERS
from lml.plugin import PluginInfo
from lml.plugin import CACHED_PLUGIN_INFO
from nose.tools import eq_, raises


def test_plugin_manager():
    test_plugin = 'my plugin'
    manager = PluginManager(test_plugin)
    assert PLUG_IN_MANAGERS[test_plugin] == manager


def test_load_me_later():
    test_plugin = 'my plugin'
    manager = PluginManager(test_plugin)
    plugin_info = make_me_a_plugin_info(test_plugin)
    manager.load_me_later(plugin_info)
    assert list(manager.registry.keys()) == [test_plugin]


@patch('lml.plugin.do_import_class')
def test_load_me_now(mock_import):
    custom_class = PluginInfo
    mock_import.return_value = custom_class
    test_plugin = 'my plugin'
    manager = PluginManager(test_plugin)
    plugin_info = make_me_a_plugin_info(test_plugin)
    manager.load_me_later(plugin_info)
    actual = manager.load_me_now(test_plugin)
    eq_(actual, custom_class)


@raises(Exception)
@patch('lml.plugin.do_import_class')
def test_load_me_now_exception(mock_import):
    custom_class = PluginInfo
    mock_import.return_value = custom_class
    test_plugin = 'my plugin'
    manager = PluginManager(test_plugin)
    plugin_info = make_me_a_plugin_info('my')
    manager.load_me_later(plugin_info)
    manager.load_me_now('my', 'my special library')


@raises(Exception)
def test_load_me_now_no_key_found():
    test_plugin = 'my plugin'
    manager = PluginManager(test_plugin)
    manager.load_me_now('my', custom_property='here')


@patch('lml.plugin.do_import_class')
def test_dynamic_load_library(mock_import):
    test_plugin = 'test plugin'
    custom_obj = object()
    mock_import.return_value = custom_obj
    manager = PluginManager(test_plugin)
    plugin_info = make_me_a_plugin_info(test_plugin)
    manager.dynamic_load_library(plugin_info)
    eq_(custom_obj, plugin_info.cls)


@patch('lml.plugin.do_import_class')
def test_dynamic_load_library_no_action(mock_import):
    test_plugin = 'test plugin'
    manager = PluginManager(test_plugin)
    plugin_info = make_me_a_plugin_info(test_plugin)
    plugin_info.cls = object()
    manager.dynamic_load_library(plugin_info)
    assert mock_import.called is False


class TestClass:
    pass


def test_register_a_plugin():
    test_plugin = 'test plugin'

    manager = PluginManager(test_plugin)
    plugin_info = make_me_a_plugin_info('my')
    manager.register_a_plugin(TestClass, plugin_info)
    eq_(plugin_info.cls, TestClass)
    eq_(manager.registry['my'][0], plugin_info)


def test_register_class():
    test_plugin = 'test_plugin'
    plugin_info = make_me_a_plugin_info('my')
    CACHED_PLUGIN_INFO[test_plugin].append(plugin_info)
    manager = PluginManager(test_plugin)
    assert list(manager.registry.keys()) == ['my']


def test_do_import():
    from lml.utils import do_import
    import pyexcel_test
    pyexcel_test_package = do_import("pyexcel_test")
    eq_(pyexcel_test_package, pyexcel_test)


@raises(ImportError)
def test_do_import_error():
    from lml.plugin import do_import
    do_import("non.exist")


def test_do_import_cls():
    from lml.plugin import do_import_class
    manager = do_import_class("lml.plugin.PluginManager")
    eq_(manager, PluginManager)


def test_load_me_later_function():
    from lml.plugin import _load_me_later
    test_plugin = 'my plugin'
    manager = PluginManager(test_plugin)
    plugin_info = make_me_a_plugin_info(test_plugin)
    _load_me_later(plugin_info)
    assert list(manager.registry.keys()) == [test_plugin]


@raises(ImportError)
def test_do_import_cls_error():
    from lml.plugin import do_import_class
    do_import_class("non.exist.class")


def test_register_a_plugin_function_1():
    PluginManager("test plugin")

    @PluginInfo('test plugin', tags=['akey'])
    class MyPlugin(object):
        pass

    MyPlugin()


@raises(Exception)
def test_register_a_plugin_function_2():

    @PluginInfo('I have no plugin manager', tags=['akey'])
    class MyPlugin(object):
        pass

    MyPlugin()


def make_me_a_plugin_info(plugin_name):
    return PluginInfo(plugin_name, 'abs_path', custom='property')
