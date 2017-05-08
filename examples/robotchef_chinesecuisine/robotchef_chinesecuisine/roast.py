from robotchef.plugin import Menu


class Roast(Menu):

    def make(self, food=None):
        print("I can roast " + food)
