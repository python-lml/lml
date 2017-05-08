from robotchef.plugin import Command


class Fry(Command):

    def action(self, food=None):
        print("I can fry " + food)
