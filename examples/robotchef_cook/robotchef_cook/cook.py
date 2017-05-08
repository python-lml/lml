from robotchef.plugin import Command


class Cook(Command):

    def action(self, food=None):
        print("I can cook " + food)
