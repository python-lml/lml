from robotchef_api.plugin import Chef


class Bake(Chef):
    def make(self, food=None):
        print("I can bake " + food)
