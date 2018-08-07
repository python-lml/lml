from lml.plugin import PluginInfoChain


__test_plugins__ = PluginInfoChain(__name__).add_a_plugin("test_io", "x")
