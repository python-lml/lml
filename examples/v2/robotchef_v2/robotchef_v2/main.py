import sys

from robotchef_api import CUISINE_MANAGER


def main():
    if len(sys.argv) < 2:
        sys.exit(-1)

    food_name = sys.argv[1]
    try:
        knowledged_chef = CUISINE_MANAGER.get_a_plugin(food_name)
        knowledged_chef.make(food=food_name)
    except Exception:
        print("I do not know how to cook " + food_name)
