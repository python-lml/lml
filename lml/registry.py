import logging
from lml.plugin import load_me_later

log = logging.getLogger(__name__)


class PluginInfo(object):
    def __init__(self, name, absolute_import_path, **keywords):
        self.name = name
        self.absolute_import_path = absolute_import_path
        self.properties = keywords

    def __getattr__(self, name):
        return self.properties.get(name)


class PluginList(object):

    def __init__(self, path):
        self.module_name = path

    def add_a_plugin(self, name, submodule,
                     file_types=None, stream_type=None):
        self._add_a_plugin(
            PluginInfo(name,
                       "%s.%s" % (self.module_name, submodule),
                       file_types=file_types,
                       stream_type=stream_type))

    def _add_a_plugin(self, plugin_info):
        log.debug(plugin_info)
        load_me_later(plugin_info)
