from robotchef.plugin import Menu


class Boost(Menu):

    def make(self, food=None, **keywords):
        print("I can cook %s for robots" % food)
