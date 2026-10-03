import random
from typing import Literal
from main_robot import Robot
from main_robot import Battery

class cleaner(Robot):
    """
This class makes a cleaner robot taht is used in teh main loop. 
It inherites name, battery, cost, dof, and task attributes from the robot class.
It has extra attributes for clean_area, premium_cleaner, clean_software_premium, and cleaner_type.
It has functions to get and set these attributes, as well as a function to perform its task
"""
    
    def __init__(self, name, battery: Battery, cost, task, clean_area, premium_cleaner, clean_software_premium, cleaner_type: Literal["basic", "fast", "large"]):
        super().__init__(name, battery, cost, None, task)
        self._clean_area = clean_area
        self._premium = premium_cleaner
        self._clean_software_premium = clean_software_premium
        self._cleaner_type = cleaner_type

    def get_clean_software_premium(self):
        return self._clean_software_premium

    def set_clean_software_premium(self, clean_software_premium):
        self._clean_software_premium = clean_software_premium

    def get_cleaner_type(self):
        return self._cleaner_type
    def set_cleaner_type(self, cleaner_type):
        if cleaner_type not in ["basic", "fast", "large"]:
            raise ValueError("Cleaner type must be 'basic', 'fast', or 'large'")
        self._cleaner_type = cleaner_type
    def get_clean_area(self):
        return self._clean_area

    def get_cost(self):
        return self._cost
    def set_cost(self, cost):
        if self._cleaner_type == "Fast":
            self._cost = 1000
        elif self._cleaner_type == "Large":
            self._cost = 2000
        else:
            self._cost = 500
        if self.get_clean_software_premium() == True:
            self._cost = self._cost * 10

    def set_clean_area(self, clean_area):
        self._clean_area = clean_area


    def do_task(self):
        self.get_battery()
        self._battery.battery_drain(20)
        if self.get_battery() < 10:
            print(f"{self._name} has blown up due to low battery")
            return
        if self._premium:
            print(f"{self._name} is cleaning the area and did a great job no errors: {self._clean_area}")
        else:
            if random.randint(1, 10) >= 80:
                print(f"{self._name} has finished cleaning but now has been lit on fire by the battery: {self._clean_area}")
            else:
                print(f"{self._name} has finished cleaning: {self._clean_area}")
            self.get_battery()

