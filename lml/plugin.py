import pkgutil
import logging
from itertools import chain
from lml.manager import load_me_later, do_import

log = logging.getLogger(__name__)


def scan_plugins(prefix, marker, path, black_list=None, white_list=None):
    if black_list is None:
        black_list = []

    if white_list is None:
        white_list = []

    # scan pkgutil.iter_modules
    module_names = (module_info[1] for module_info in pkgutil.iter_modules()
                    if module_info[2] and module_info[1].startswith(prefix))

    # scan pyinstaller
    module_names_from_pyinstaller = scan_from_pyinstaller(prefix, path)

    all_modules = chain(module_names,
                        module_names_from_pyinstaller,
                        white_list)
    # loop through modules and find our plug ins
    for module_name in all_modules:

        if module_name in black_list:
            continue

        try:
            load_plugins(module_name, marker)
        except ImportError as e:
            log.debug(module_name)
            log.debug(e)
            continue


# load modules to work based with and without pyinstaller
# from: https://github.com/webcomics/dosage/blob/master/dosagelib/loader.py
# see: https://github.com/pyinstaller/pyinstaller/issues/1905
# load modules using iter_modules()
# (should find all plug ins in normal build, but not pyinstaller)
def scan_from_pyinstaller(prefix, path):
    # special handling for PyInstaller
    table_of_content = set()
    for a_toc in (importer.toc for importer in map(pkgutil.get_importer, path)
                  if hasattr(importer, 'toc')):
        table_of_content |= a_toc

    for module_name in table_of_content:
        if module_name.startswith(prefix) and '.' not in module_name:
            yield module_name


def load_plugins(plugin_module_name, marker):
    plugin_module = do_import(plugin_module_name)
    if hasattr(plugin_module, marker):
        for plugin_meta in getattr(plugin_module, marker):
            load_me_later(plugin_meta, plugin_module_name)
