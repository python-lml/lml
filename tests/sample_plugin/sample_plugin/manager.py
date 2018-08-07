from lml.plugin import PluginManager


class TestPluginManager(PluginManager):
    def __init__(self):
        PluginManager.__init__(self, "test_io2")

    def load_me_later(self, plugin_info):
        PluginManager.load_me_later(self, plugin_info)

    def register_a_plugin(self, cls):
        PluginManager.register_a_plugin(self, cls)


testmanager = TestPluginManager()
