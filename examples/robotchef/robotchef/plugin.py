from lml.plugin import PluginManager


class CuisineManager(PluginManager):
    def __init__(self):
        PluginManager.__init__(self, "cuisine")

    def get_a_plugin(self, command=None, **keywords):
        return PluginManager.get_a_plugin(self, key=command, **keywords)


class Menu(object):

    def make(self, **params):
        print(self.name)
