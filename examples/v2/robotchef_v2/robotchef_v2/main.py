import sys

from robotchef_api import cuisine_manager, NoChefException


def main():
    if len(sys.argv) < 2:
        sys.exit(-1)

    food_name = sys.argv[1]
    try:
        knowledged_chef = cuisine_manager.get_a_plugin(food_name)
        knowledged_chef.make(food=food_name)
    except NoChefException:
        print("I do not know how to cook " + food_name)
