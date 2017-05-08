from robotchef.plugin import Menu


class Menu(Command):

    def make(self, food=None):
        print("I can bake " + food)
