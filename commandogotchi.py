import datetime


class Commandogotchi:
    def __init__(self, name, age=0, hunger=0, happiness=0, health=0,
                 growth=0, weight=0, discipline=0):
        self.name = name
        self.age = age
        self.hunger = hunger
        self.happiness = happiness
        self.health = health
        self.growth = growth
        self.weight = weight
        self.discipline = discipline
        self.birth_time = datetime.datetime.now()

    def hunger_gain(self, hunger):
        pass

    def update_age(self, age, birth_time):
        self.age = datetime.datetime.now() - birth_time
        return self.age
