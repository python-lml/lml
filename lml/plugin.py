import pkgutil
from itertools import chain
from lml.manager import plugin_first


def scan_plugins(prefix, marker, path, black_list):
    # scan pkgutil.iter_modules
    module_names = (module_info[1] for module_info in pkgutil.iter_modules()
                    if module_info[2] and module_info[1].startswith(prefix))

    # scan pyinstaller
    module_names_from_pyinstaller = scan_from_pyinstaller(prefix, path)
    # loop through modules and find our plug ins
    for module_name in chain(module_names, module_names_from_pyinstaller):

        if module_name in black_list:
            continue

        try:
            plugin = __import__(module_name)
            if hasattr(plugin, marker):
                for plugin_meta in getattr(plugin, marker):
                    plugin_first(plugin_meta, module_name)
        except ImportError:
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
