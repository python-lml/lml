from robotchef.plugin import Chef


class Cook(Chef):

    def make(self, food=None):
        print("I can cook " + food)
