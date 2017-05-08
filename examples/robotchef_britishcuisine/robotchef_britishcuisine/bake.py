from robotchef.plugin import Menu


class Bake(Menu):

    def make(self, food=None):
        print("I can bake " + food)
