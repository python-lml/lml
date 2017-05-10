from lml.loader import scan_plugins
from robotchef_api.plugin import CuisineManager


BUILTINS = ['robotchef.robot_cuisine']


scan_plugins("robotchef_", __path__, white_list=BUILTINS)
CUISINE_MANAGER = CuisineManager()
