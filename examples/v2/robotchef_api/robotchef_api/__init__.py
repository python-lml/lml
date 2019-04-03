from lml.loader import scan_plugins_regex
from robotchef_api.plugin import CuisineManager, NoChefException  # noqa: F401


BUILTINS = ["robotchef_api.robot_cuisine"]


scan_plugins_regex(
    plugin_name_patterns="^robotchef_*$",
    pyinstaller_path=__path__,  # noqa: F821
    white_list=BUILTINS)
cuisine_manager = CuisineManager()
