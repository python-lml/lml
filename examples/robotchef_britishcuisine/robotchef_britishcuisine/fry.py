from robotchef.plugin import Menu


class Fry(Menu):

    def make(self, food=None):
        print("I can fry " + food)
