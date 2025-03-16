"""
    lml.utils
    ~~~~~~~~~~~~~~~~~~~

    json utils for dump plugin info class

    :copyright: (c) 2017-2025 by C.W.
    :license: New BSD License, see LICENSE for more details
"""
import logging
import importlib
from json import JSONEncoder, dumps

log = logging.getLogger(__name__)


class PythonObjectEncoder(JSONEncoder):
    """
    Custom object encoder for json dump
    """

    def default(self, obj):
        a_list_of_types = (list, dict, str, int, float, bool, type(None))
        if isinstance(obj, a_list_of_types):
            return JSONEncoder.default(self, obj)
        return {"_python_object": str(obj)}


def json_dumps(keywords):
    """
    Dump function keywords in json
    """
    return dumps(keywords, cls=PythonObjectEncoder)


def do_import(plugin_module_name):
    """dynamically import a module"""
    try:
        return _do_import(plugin_module_name)
    except ImportError:
        log.exception("%s is absent or cannot be imported", plugin_module_name)
        raise


def _do_import(plugin_module_name):
    plugin_module = importlib.import_module(plugin_module_name)
    log.debug("found " + plugin_module_name)
    return plugin_module


def do_import_class(plugin_class):
    """dynamically import a class"""
    try:
        plugin_module_name, class_name = plugin_class.rsplit(".", 1)
        plugin_module = importlib.import_module(plugin_module_name)
        cls = getattr(plugin_module, class_name)
        return cls
    except ImportError:
        log.exception("Failed to import %s", plugin_module_name)
        raise
