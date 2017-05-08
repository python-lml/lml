import sys

import logging
import logging.config

from robotchef.plugin import CuisineManager

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG)


def main():
    if len(sys.argv) < 2:
        sys.exit(-1)

    manager = CuisineManager()
    food_name = sys.argv[1]
    try:
        knowledged_chef = manager.get_a_plugin(food_name)
        print(knowledged_chef.make(food=food_name))
    except Exception:
        print("I do not know how to cook " + food_name)
