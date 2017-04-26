from lml.registry import PluginList


__test_plugins__ = PluginList(__name__).add_a_plugin(
    'test_io2', 'reader')
