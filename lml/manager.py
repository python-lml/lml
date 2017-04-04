PLUG_IN_MANAGERS = {}


def register_class(cls):
    PLUG_IN_MANAGERS[cls.name] = cls


class PluginManager(object):
    name = "plugin"

    def plugin_first(self, meta, module_name):
        pass

    def list_registry(self):
        pass

    def load_me_later(self, registry_key):
        pass

    def plugin_now(self, cls):
        pass

    def get_plugin(self):
        pass


def plugin_first(meta, module_name):
    manager = PLUG_IN_MANAGERS.get(meta['plugin_type'])
    manager.plugin_first(meta, module_name)


