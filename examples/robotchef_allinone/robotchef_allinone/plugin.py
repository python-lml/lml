class NoChefException(Exception):
    pass


class Chef(object):
    def make(self, **params):
        print("I am a chef")


class Boost(Chef):
    def make(self, food=None, **keywords):
        print("I can cook %s for robots" % food)


class Fry(Chef):
    def make(self, food=None):
        print("I can fry " + food)


class Bake(Chef):
    def make(self, food=None):
        print("I can bake " + food)


PLUGINS = {
    "Portable Battery": Boost,
    "Fish and Chips": Fry,
    "Cornish Scone": Bake,
    "Jacket Potato": Bake,
}


def get_a_plugin(food_name=None, **keywords):
    plugin = PLUGINS.get(food_name)
    if plugin is None:
        raise NoChefException("Cannot find a chef")
    plugin_cls = plugin()
    return plugin_cls
