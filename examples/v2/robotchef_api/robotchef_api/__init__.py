from lml.loader import scan_plugins
from robotchef_api.plugin import CuisineManager, NoChefException  # noqa: F401


BUILTINS = ["robotchef_api.robot_cuisine"]


scan_plugins("robotchef_", __path__, white_list=BUILTINS)  # noqa: F821
cuisine_manager = CuisineManager()
