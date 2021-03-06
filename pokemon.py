#!/usr/bin/python3
""" creates a simple pokedex and pokemon game """""""""
import numpy as np
import time


class Pokemon:
    round = 0

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
        if type(value) is not str:
            raise TypeError("Name should be letters")
        else:
            self.__name = value

    @property
    def number(self):
        """ Index in the pokedex """
        return self.__number

    @number.setter
    def number(self, value):
        if type(value) is not int:
            raise TypeError("Number must be an integer")
        else:
            self.__number = value

    @property
    def type(self):
        """ Pokemon type """
        return self.__type

    @type.setter
    def type(self, value):
        if type(value) is not str:
            raise TypeError("Pokemon type must be watger, earth, fire, \
                 wind or bug")
        else:
            self.__type = value

    @property
    def weight(self):
        """ Weight of the pokemon """
        return self.__weight

    @weight.setter
    def weight(self, value):
        if type(value) is not (int or float):
            raise TypeError("Weight must be an integer or a float")
        else:
            self.__weight = value

    @property
    def height(self):
        """ Height of the pokemon """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not (int or float):
            raise TypeError("Height must be an integer or a float")
        else:
            self.__height = value

    @property
    def attack(self):
        """ Attack value """
        return self.__attack

    @attack.setter
    def attack(self, value):
        self.__attack = value

    def combat(self, opponent):
        while (self.__HP > 0) and (opponent.__HP > 0):
            print("-------ROUND {:d}------".format(Pokemon.round), end="\n")
            print(f"{self.name}, hit points are {self.__HP} &", end=" ")
            print(f"{opponent.name}, hit points are {opponent.__HP}")
            time.sleep(2)
            print(f"{self.name} go!", end=" ")
            opponent.__HP -= self.attack
            if opponent.__HP <= 0:
                print(f"{opponent.name} fainted!")
                break
            else:
                print(f"{opponent.name} go!")
                self.__HP -= opponent.attack
                if self.__HP <= 0:
                    print(f"{self.name} fainted!")
                    break
            Pokemon.round += 1
            time.sleep(3)


if __name__ == "__main__":
    Skrelp = Pokemon('Skrelp', '690', 'water', '0.8', '7.30')
    Masquerain = Pokemon('Masquerain', '284', 'bug', '0.30', '3.5')

    # Combat
    Skrelp.combat(Masquerain)
