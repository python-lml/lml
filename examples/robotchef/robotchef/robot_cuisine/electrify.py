from robotchef.plugin import Chef


class Boost(Chef):
    def make(self, food=None, **keywords):
        print("I can cook %s for robots" % food)
