class Hero:
    def __init__(self, name, abyliti):
        self.name = name
        self.abyliti = abyliti


class HeroSuper(Hero):
    def __str__(self):
        return f'it is {self.name}'

    def display_info(self):
        print(self.__str__())

