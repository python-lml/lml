from robotchef_api.plugin import Chef


class Fry(Chef):

    def make(self, food=None):
        print("I can fry " + food)
