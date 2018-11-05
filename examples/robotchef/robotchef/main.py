import sys
import logging
import logging.config

from lml.loader import scan_plugins
from robotchef.plugin import CuisineManager, NoChefException

logging.basicConfig(
    format="%(name)s:%(lineno)d - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)

BUILTINS = ["robotchef.robot_cuisine"]


def main():
    if len(sys.argv) < 2:
        sys.exit(-1)

    cuisine_manager = CuisineManager()
    scan_plugins("robotchef_", "robotchef", white_list=BUILTINS)

    food_name = sys.argv[1]
    try:
        knowledged_chef = cuisine_manager.get_a_plugin(food_name)
        knowledged_chef.make(food=food_name)
    except NoChefException:
        print("I do not know how to cook " + food_name)
