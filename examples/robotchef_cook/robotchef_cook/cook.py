from robotchef.plugin import Menu


class Cook(Menu):

    def make(self, food=None):
        print("I can cook " + food)
