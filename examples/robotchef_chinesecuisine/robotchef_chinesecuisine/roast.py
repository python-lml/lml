from robotchef.plugin import Chef


class Roast(Chef):

    def make(self, food=None):
        print("I can roast " + food)
