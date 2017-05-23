from lml.plugin import PluginManager, PluginInfo


class NoChefException(Exception):
    pass


class CuisineManager(PluginManager):
    def __init__(self):
        PluginManager.__init__(self, "cuisine")

    def get_a_plugin(self, food_name=None, **keywords):
        return PluginManager.get_a_plugin(self, key=food_name, **keywords)

    def raise_exception(self, key):
        raise NoChefException("Cannot find a chef")


class Chef(object):

    def make(self, **params):
        print("I am a chef")


@PluginInfo('cuisine', tags=['Portable Battery'])
class Boost(Chef):

    def make(self, food=None, **keywords):
        print("I can cook %s for robots" % food)


@PluginInfo('cuisine', tags=['Fish and Chips'])
class Fry(Chef):

    def make(self, food=None):
        print("I can fry " + food)


@PluginInfo('cuisine', tags=['Cornish Scone', 'Jacket Potato'])
class Bake(Chef):

    def make(self, food=None):
        print("I can bake " + food)
