from lml.manager import PluginList, PluginInfo


__test_plugins__ = PluginList(__name__)._add_a_plugin(
    PluginInfo(
        plugin_type='test_io',
        submodule='x'
    )
)
