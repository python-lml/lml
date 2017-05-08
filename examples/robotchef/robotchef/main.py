import logging
import logging.config
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG)

import sys
from lml.plugin import PluginManager
from lml.loader import scan_plugins


class RobotCommandManager(PluginManager):
    def __init__(self):
        PluginManager.__init__(self, "robot")

    def get_a_plugin(self, command=None, **keywords):
        return PluginManager.get_a_plugin(self, key=command, **keywords)


manager = RobotCommandManager()

scan_plugins(
    "robotchef_", ".",
    black_list=None, white_list=None)


def main():
    if len(sys.argv) < 2:
        sys.exit(-1)

    command = sys.argv[1]
    commando = manager.get_a_plugin(command)
    print(commando.action(food=command))
