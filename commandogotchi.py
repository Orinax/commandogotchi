from time import sleep
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


    def hunger_gain(self, hunger):
        pass


    def get_birth_time(self, age, datetime):
        birth_time = datetime.datetime.now()
        return birth_time

    def show_current_age(self, age, birth_time, datetime):
        current_age = datetime.datetime.now() - birth_time
        return current_age
