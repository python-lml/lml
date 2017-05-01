from mock import patch
from lml.plugin import PluginManager, PLUG_IN_MANAGERS
from lml.registry import PluginInfo
from nose.tools import eq_, raises


def test_plugin_manager():
    test_plugin = 'my plugin'
    manager = PluginManager(test_plugin)
    assert PLUG_IN_MANAGERS[test_plugin] == manager


def test_load_me_later():
    test_plugin = 'my plugin'
    manager = PluginManager(test_plugin)
    plugin_info = PluginInfo('my', 'abs_path', custom='property')
    manager.load_me_later(plugin_info)
    assert list(manager.registry.keys()) == ['my']


@patch('lml.plugin.do_import_class')
def test_load_me_now(mock_import):
    custom_class = PluginInfo
    mock_import.return_value = custom_class
    test_plugin = 'my plugin'
    manager = PluginManager(test_plugin)
    plugin_info = PluginInfo('my', 'abs_path', custom='property')
    manager.load_me_later(plugin_info)
    actual = manager.load_me_now('my')
    eq_(actual, custom_class)


@raises(Exception)
@patch('lml.plugin.do_import_class')
def test_load_me_now_exception(mock_import):
    custom_class = PluginInfo
    mock_import.return_value = custom_class
    test_plugin = 'my plugin'
    manager = PluginManager(test_plugin)
    plugin_info = PluginInfo('my', 'abs_path', custom='property')
    manager.load_me_later(plugin_info, 'my special library')
    actual = manager.load_me_now('my')
    eq_(actual, custom_class)
