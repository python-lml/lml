import logging
from collections import defaultdict

PLUG_IN_MANAGERS = {}
CACHED_PLUGIN_INFO = defaultdict(list)

log = logging.getLogger(__name__)


class PluginManager(object):

    def __init__(self, plugin_name):
        self.plugin_name = plugin_name
        self.registry = defaultdict(list)
        self._logger = logging.getLogger(
            self.__class__.__module__ + '.' + self.__class__.__name__)
        register_class(self)

    def load_me_later(self, plugin_info):
        self._logger.debug('load me later: ' + plugin_info.module_name)
        self._logger.debug(plugin_info)
        for file_type in plugin_info.keywords():
            self._logger.debug('======>'+file_type)
            self.registry[file_type].append(plugin_info)

    def load_me_now(self, key, library=None, **keywords):
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
                if library:
                    raise Exception("%s is not installed" % library)
                else:
                    self.raise_exception(key)
            return cls
        else:
            self.raise_exception(key)

    def raise_exception(self, key):
        raise Exception(
            "No %s is found for %s" % (self.name, key))

    def dynamic_load_library(self, a_plugin_info):
        self._logger.debug("import " + a_plugin_info.absolute_import_path)
        if a_plugin_info.cls is None:
            cls = do_import_class(a_plugin_info.absolute_import_path)
            a_plugin_info.cls = cls
        return a_plugin_info.cls

    def register_a_plugin(self, cls, plugin_info):
        """ for dynamically loaded plugin """
        self._logger.debug("register " + cls.__name__)
        for key in plugin_info.keywords():
            self.registry[key.lower()].append(cls)

    def get_a_plugin(self, **keywords):
        self._logger.debug("get a plugin: ")


def register_class(cls):
    log.debug("register " + cls.plugin_name)
    PLUG_IN_MANAGERS[cls.plugin_name] = cls
    if cls.plugin_name in CACHED_PLUGIN_INFO:
        # check if there is early registrations or not
        for plugin_info in CACHED_PLUGIN_INFO[cls.plugin_name]:
            log.debug("load cached values " + plugin_info.absolute_import_path)
            cls.load_me_later(plugin_info)

        del CACHED_PLUGIN_INFO[cls.plugin_name]


class Plugin(type):
    """sole class registry"""
    def __init__(cls, name, bases, nmspc):
        super(Plugin, cls).__init__(
            name, bases, nmspc)
        register_a_plugin(cls)


def register_a_plugin(cls):
    manager = PLUG_IN_MANAGERS.get(cls.plugin_name)
    if manager:
        manager.register_a_plugin(cls, cls)
    else:
        raise Exception("%s has no registry" % cls.plugin_name)


def load_me_later(plugin_info):
    log.debug("load me later")
    log.debug(plugin_info)
    manager = PLUG_IN_MANAGERS.get(plugin_info.name)
    if manager:
        manager.load_me_later(plugin_info)
    else:
        # let's cache it and wait the manager to be registered
        log.debug("caching " + plugin_info.absolute_import_path)
        CACHED_PLUGIN_INFO[plugin_info.name].append(plugin_info)


def do_import(plugin_module_name):
    try:
        log.debug("do import " + plugin_module_name)
        plugin_module = __import__(plugin_module_name)
        if '.' in plugin_module_name:
            modules = plugin_module_name.split('.')
            for module in modules[1:]:
                plugin_module = getattr(plugin_module, module)
        return plugin_module
    except ImportError:
        log.debug("Failed to import %s" % plugin_module_name)
        raise


def do_import_class(plugin_class):
    try:
        plugin_module_name = plugin_class.rsplit('.', 1)[0]
        plugin_module = __import__(plugin_module_name)
        modules = plugin_class.split('.')
        for module in modules[1:]:
            plugin_module = getattr(plugin_module, module)
        return plugin_module
    except ImportError:
        log.debug("Failed to import %s" % plugin_module_name)
        raise


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
