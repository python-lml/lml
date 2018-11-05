from lml.loader import scan_plugins
from robotchef_api.plugin import (
    CuisineManager,
    NoChefException,
)  # flake8: noqa


BUILTINS = ["robotchef_api.robot_cuisine"]


scan_plugins("robotchef_", __path__, white_list=BUILTINS)
cuisine_manager = CuisineManager()
