"""
    lml.plugin
    ~~~~~~~~~~~~~~~~~~~

    Plugin management system

    :copyright: (c) 2017 by Onni Software Ltd.
    :license: New BSD License, see LICENSE for more details
"""
import logging
from collections import defaultdict

from lml.utils import do_import_class


PLUG_IN_MANAGERS = {}
CACHED_PLUGIN_INFO = defaultdict(list)

log = logging.getLogger(__name__)


class PluginManager(object):
    """
    Load plugin info into in-memory dictionary for later import
    """
    def __init__(self, plugin_name):
        self.plugin_name = plugin_name
        self.registry = defaultdict(list)
        self._logger = logging.getLogger(
            self.__class__.__module__ + '.' + self.__class__.__name__)
        register_class(self)

    def load_me_later(self, plugin_info):
        """
        Register a plugin info for later loading
        """
        self._logger.debug('load me later: ' + plugin_info.module_name)
        self._logger.debug(plugin_info)
        for key in plugin_info.keywords():
            self.registry[key.lower()].append(plugin_info)

    def load_me_now(self, key, library=None, **keywords):
        """
        Import a plugin from plugin registry
        """
        self._logger.debug("load me now:" + key)
        if keywords:
            self._logger.debug(keywords)
        __key = key.lower()
        if __key in self.registry:
            for plugin_info in self.registry[__key]:
                cls = self.dynamic_load_library(plugin_info)
                module_name = _get_me_pypi_package_name(cls.__module__)
                if library and module_name != library:
                    continue
                else:
                    break
            else:
                # only library condition coud raise an exception
                raise Exception("%s is not installed" % library)
            return cls
        else:
            self.raise_exception(key)

    def raise_exception(self, key):
        """Raise plugin not found exception"""
        self._logger.debug(self.registry.keys())
        raise Exception(
            "No %s is found for %s" % (self.plugin_name, key))

    def dynamic_load_library(self, a_plugin_info):
        """Dynamically load the plugin info if not loaded"""
        self._logger.debug("import " + a_plugin_info.absolute_import_path)
        if a_plugin_info.cls is None:
            cls = do_import_class(a_plugin_info.absolute_import_path)
            a_plugin_info.cls = cls
        return a_plugin_info.cls

    def register_a_plugin(self, cls, plugin_info):
        """ for dynamically loaded plugin during runtime"""
        self._logger.debug("register " + cls.__name__)
        for key in plugin_info.keywords():
            plugin_info.cls = cls
            self.registry[key.lower()].append(plugin_info)

    def get_a_plugin(self, key, **keywords):
        """ Get a plugin """
        self._logger.debug("get a plugin")
        plugin = self.load_me_now(key)
        return plugin()


def register_class(cls):
    """Reigister a newly created plugin manager"""
    log.debug("register " + cls.plugin_name)
    PLUG_IN_MANAGERS[cls.plugin_name] = cls
    if cls.plugin_name in CACHED_PLUGIN_INFO:
        # check if there is early registrations or not
        for plugin_info in CACHED_PLUGIN_INFO[cls.plugin_name]:
            log.debug("load cached values " + plugin_info.absolute_import_path)
            cls.load_me_later(plugin_info)

        del CACHED_PLUGIN_INFO[cls.plugin_name]


class Plugin(type):
    """
    For ad-hoc plugin classes

    In a situation where the intention is not to redistribute
    a plugin package, a dynamically written class is written
    as one off attempt to extend the main package.
    """
    def __init__(cls, name, bases, nmspc):
        super(Plugin, cls).__init__(
            name, bases, nmspc)
        register_a_plugin(cls)


def register_a_plugin(cls):
    """module level function to register a plugin"""
    manager = PLUG_IN_MANAGERS.get(cls.plugin_name)
    if manager:
        manager.register_a_plugin(cls, cls)
    else:
        raise Exception("%s has no registry" % cls.plugin_name)


def load_me_later(plugin_info):
    """ module level function to load a plugi later"""
    log.debug("load me later")
    log.debug(plugin_info)
    manager = PLUG_IN_MANAGERS.get(plugin_info.name)
    if manager:
        manager.load_me_later(plugin_info)
    else:
        # let's cache it and wait the manager to be registered
        log.debug("caching " + plugin_info.absolute_import_path)
        CACHED_PLUGIN_INFO[plugin_info.name].append(plugin_info)


def with_metaclass(meta, *bases):
    # This requires a bit of explanation: the basic idea is to make a
    # dummy metaclass for one level of class instantiation that replaces
    # itself with the actual metaclass.  Because of internal type checks
    # we also need to make sure that we downgrade the custom metaclass
    # for one level to something closer to type (that's why __call__ and
    # __init__ comes back from type etc.).
    #
    # This has the advantage over six.with_metaclass in that it does not
    # introduce dummy classes into the final MRO.
    # :copyright: (c) 2014 by Armin Ronacher.
    # :license: BSD, see LICENSE for more details.
    class metaclass(meta):
        __call__ = type.__call__
        __init__ = type.__init__

        def __new__(cls, name, this_bases, d):
            if this_bases is None:
                return type.__new__(cls, name, (), d)
            return meta(name, bases, d)
    return metaclass('temporary_class', None, {})


def _get_me_pypi_package_name(module_name):
    root_module_name = module_name.split('.')[0]
    return root_module_name.replace('_', '-')
