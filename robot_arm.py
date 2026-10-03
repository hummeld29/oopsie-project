from main_robot import Robot
from typing import Literal
import random
from main_robot import Battery

class Robot_dog(Robot):
    """
This classs creates a robot dog.
This class inherits name, battery, cost, dof, and task attributes from the Robot class.
It has additional attributes for size, training, and training cost.
It has functions to get and set these attributes, as well as a function to perform its task.
"""

    def __init__(self, name, battery: Battery, cost, dof, task, size: Literal["small", "medium", "large", "extra_large"], training=None, training_cost=0 ):
        super().__init__(name, battery, cost, dof, task)
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
        import random

        print(f"{self._name} is playing with its {self._size} body.")
        self._battery.battery_drain(20)
        if self.get_battery() < 10:
            print(f"{self._name} has sadly blown up due to low battery")
            return
        if not self._training: 
            
            roll = random.randint(1, 100)      
            if roll == 1:
                print(f"{self._name} has gotten hit by a car.")
            
                survival_roll = random.randint(1, 100)
                if survival_roll <= 50:
                    print(f"{self._name} is fine.")
                else:
                    print(f"{self._name} is broken.")
                    
            elif roll >= 80:
                # 4. Connected with 'elif' so it doesn't happen at the same time as the car
                print(f"{self._name} has gotten into an accident with itself.")
                
            else:
                # If neither bad event happens, it plays safely
                print(f"{self._name} is safely playing with its {self._size} body.")
                
        else:
            # If the dog is trained, it bypasses the accidents entirely
            print(f"{self._name} is safely playing with its {self._size} body.")
