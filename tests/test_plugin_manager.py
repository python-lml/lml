from lml.plugin import PluginManager, PLUG_IN_MANAGERS


def test_plugin_manager():
    test_plugin = 'my plugin'
    manager = PluginManager(test_plugin)
    assert PLUG_IN_MANAGERS[test_plugin] == manager
