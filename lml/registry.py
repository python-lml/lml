import logging

from lml.plugin import load_me_later
from lml.utils import json_dumps

log = logging.getLogger(__name__)


class PluginInfo(object):
    def __init__(self, name, absolute_import_path, **keywords):
        self.name = name
        self.absolute_import_path = absolute_import_path
        self.cls = None
        self.properties = keywords

    def __getattr__(self, name):
        if name == 'module_name':
            module_name = self.absolute_import_path.split('.')[0]
            return module_name
        return self.properties.get(name)

    def keywords(self):
        yield self.name

    def __repr__(self):
        rep = {"name": self.name, "path": self.absolute_import_path}
        rep.update(self.properties)
        return json_dumps(rep)


class PluginList(object):

    def __init__(self, path):
        self.module_name = path

    def add_a_plugin(self, name, submodule=None,
                     **keywords):
        a_plugin_info = PluginInfo(name,
                                   self._get_abs_path(submodule),
                                   **keywords)

        self._add_a_plugin(a_plugin_info)
        return self

    def _add_a_plugin(self, plugin_info_instance):
        log.debug(plugin_info_instance)
        load_me_later(plugin_info_instance)
        return self

    def _get_abs_path(self, submodule):
        return "%s.%s" % (self.module_name, submodule)
