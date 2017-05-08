from robotchef.plugin import Command


class Bake(Command):

    def action(self, food=None):
        print("I can bake " + food)
