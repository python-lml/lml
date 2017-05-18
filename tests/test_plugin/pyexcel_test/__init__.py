from lml.registry import PluginInfoList


__test_plugins__ = PluginInfoList(__name__).add_a_plugin(
    'test_io', 'x')
