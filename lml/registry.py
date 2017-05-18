"""
    lml.registry
    ~~~~~~~~~~~~~~~~~~~

    Handle plugin registration

    :copyright: (c) 2017 by Onni Software Ltd.
    :license: New BSD License, see LICENSE for more details
"""
import logging

from lml.plugin import load_me_later
from lml.utils import json_dumps

log = logging.getLogger(__name__)


class PluginInfo(object):
    """
    Information about the plugin

    Parameters
    -------------
    name:
       plugin name

    absolute_import_path:
       absolute import path from your plugin name space for your plugin class

    tags:
       a list of keywords help the plugin manager to retrieve your plugin
    """
    def __init__(self, name, absolute_import_path, tags=None, **keywords):
        self.name = name
        self.absolute_import_path = absolute_import_path
        self.cls = None
        self.properties = keywords
        self.tags = tags

    def __getattr__(self, name):
        if name == 'module_name':
            module_name = self.absolute_import_path.split('.')[0]
            return module_name
        return self.properties.get(name)

    def keywords(self):
        """
        A list of tags for identifying the plugin class

        The plugin class is described at the absolute_import_path
        """
        if self.tags is None:
            yield self.name
        else:
            for tag in self.tags:
                yield tag

    def __repr__(self):
        rep = {"name": self.name, "path": self.absolute_import_path}
        rep.update(self.properties)
        return json_dumps(rep)


class PluginInfoList(object):
    """
    Pandas style, chained list declaration

    It is used in the plugin packages to list all plugin classes
    """
    def __init__(self, path):
        self.module_name = path

    def add_a_plugin(self, name, submodule=None,
                     **keywords):
        """
        Add a plain plugin

        Parameters
        -------------

        name:
          plugin manager name

        submodule:
          the relative import path to your plugin class
        """
        a_plugin_info = PluginInfo(
            name,
            self._get_abs_path(submodule),
            **keywords)

        self.add_a_plugin_instance(a_plugin_info)
        return self

    def add_a_plugin_instance(self, plugin_info_instance):
        """
        Add a plain plugin

        Parameters
        -------------

        plugin_info_instance:
          an instance of PluginInfo

        The developer has to specify the absolute import path
        """
        log.debug(plugin_info_instance)
        load_me_later(plugin_info_instance)
        return self

    def _get_abs_path(self, submodule):
        return "%s.%s" % (self.module_name, submodule)
