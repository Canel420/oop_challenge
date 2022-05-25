#!/usr/bin/python3
""" creates a simple pokedex and pokemon game """""""""
import numpy as np
import time


class Pokemon:
    def __init__(self, name, number, type, height, weight):
        """ Defines pokemon class """


        self.__name = name
        self.__number = number
        self.__type = type
        self.__height = height
        self.__weight = weight
        self.__HP = 15
        self.__attack = np.random.choice([x for x in range(1, 10)], 1)

    @property
    def name(self):
        """ Name of the pokemon """
        return self.__name

    @name.setter
    def name(self, value):
        self.__name

    @property
    def number(self):
        """ Index in the pokedex """
        return self.__number

    @number.setter
    def number(self, value):
        self.__number

    @property
    def type(self):
        """ Pokemon type """
        return self.__type

    @type.setter
    def type(self, value):
        self.__type

    @property
    def weight(self):
        """ Weight of the pokemon """
        return self.__weight

    @weight.setter
    def weight(self, value):
        self.__weight

    @property
    def height(self):
        """ Height of the pokemon """
        return self.__height

    @height.setter
    def height(self, value):
        self.__height

    @property
    def attack(self):
        """ Attack value """
        return self.__attack

    @attack.setter
    def attack(self, value):
        self.__attack

    def combat(self, opponent):
        while (self.HP > 0) and (opponent.HP > 0):
            print(f"{self.name}, hit points are {self.HP}")
            print(f"{opponent.name}, hit points are {opponent.HP}")
            time.sleep(2)
            print(f"{self.name} go!")
            opponent.HP -= self.attack
            if opponent.HP <= 0:
                print(f"{opponent.name} fainted!")
                break
            else:
                print(f"{opponent.name} go!")
                self.HP -= opponent.attack
                if self.HP <= 0:
                    print(f"{self.name} fainted!")
                    break               
            time.sleep(3)

if __name__ == "__main__":
    Skrelp = Pokemon('Skrelp', '690', 'water', '0.8', '7.30')
    Masquerain = Pokemon('Masquerain', '284', 'bug', '0.30', '3.5')
