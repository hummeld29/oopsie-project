from main_robot import Robot
from typing import Literal
from pydantic import BaseModel, ValidationError
from random import random

class Robot_dog(Robot):
    def __init__(self, name, battery_percent, cost, dof, task, size: Literal["small", "medium", "large", "extra_large"], training=None, training_cost=0 ):
        super().__init__(name, battery_percent, cost, dof, task)
        self._size = size
        self._training = training
        self._training_cost = training_cost

    def get_size(self):
        return self._size
    def set_size(self, size):
        if size not in ["small", "medium", "large", "extra_large"]:
            raise ValueError("Size must be 'small', 'medium', 'large', or 'extra_large'")
        self._size = size
    def set_training(self, training):
        self._training = True
    def get_training(self):
        return self._training
    def training_cost(self):
        if self._size == "small":
            return self._training_cost == 1000
        elif self._size == "medium":
            return self._training_cost == 1500
        elif self._size == "large":
            return self._training_cost == 2000
        elif self._size == "extra_large":
            return self._training_cost == 3000
    def get_cost(self):
        return self._cost
    def set_cost(self, cost):
        if self._size == "small":
            self._cost = 10000
        elif self._size == "medium":
            self._cost = 15000
        elif self._size == "large":
            self._cost = 20000
        elif self._size == "extra_large":
            self._cost = 30000

    def do_task(self):
        print(f"{self._name} is playing with its {self._size} body.")
        if random.randint(1,100) == 1and self._training == None:
            print(f"{self._name} has gotten hit by a car.")
            if random.randint(1,100) < 50:
                print(f"{self._name} is fine.")
            elif random.randint(1,100) > 50:
                print(f"{self._name} is broken.")
        if random.randint(1, 100) >= 80 and self._training == None:
            print(f"{self._name} has gotten into an accident with its self")
        else:
            print(f"{self._name} is safely playing with its {self._size} body.")