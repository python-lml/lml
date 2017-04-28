import logging
from json import dumps, JSONEncoder

from lml.plugin import load_me_later
from lml._compact import PY2

log = logging.getLogger(__name__)


class PythonObjectEncoder(JSONEncoder):
    def default(self, obj):
        a_list_of_types = (list, dict, str,
                           int, float, bool, type(None))
        if PY2:
            a_list_of_types += (unicode,)
        if isinstance(obj, a_list_of_types):
            return JSONEncoder.default(self, obj)
        return {'_python_object': str(obj)}


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
        return dumps(rep, cls=PythonObjectEncoder)


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
        load_me_later(plugin_info_instance)
        return self

    def _get_abs_path(self, submodule):
        return "%s.%s" % (self.module_name, submodule)
