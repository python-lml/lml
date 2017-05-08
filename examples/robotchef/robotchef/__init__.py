from lml.loader import scan_plugins


BUILTINS = ['robotchef.robot_cuisine']


scan_plugins("robotchef_", ".", white_list=BUILTINS)
