import random
from typing import Literal
from main_robot import Robot
from main_robot import Battery

class cleaner(Robot):
"""
This class makes a cleaner robot taht is used in teh main loop. 
It inherites _____ from the robot class.

"""
    
    def __init__(self, name,battery: Battery , cost, task, clean_area, premium_cleaner, clean_software_quality, cleaner_type: Literal["basic", "fast", "large"]):
        super().__init__(name, battery, cost, task)
        self._clean_area = clean_area
        self._premium = premium_cleaner
        self._clean_software_quality = clean_software_quality
        self._cleaner_type = cleaner_type

    def get_clean_software_quality(self):
        return self._clean_software_quality

    def set_clean_software_quality(self, clean_software_quality):
        self._clean_software_quality = True

    def get_cleaner_type(self):
        return self._cleaner_type
    def set_cleaner_type(self, cleaner_type):
        if cleaner_type not in ["basic", "fast", "large"]:
            raise ValueError("Cleaner type must be 'basic', 'fast', or 'large'")
        self._cleaner_type = cleaner_type
    def get_clean_area(self):
        return self._clean_area

    def get_premium(self):
        return self._premium
    def set_premium(self, premium):
        self._premium = True
    def get_cost(self):
        return self._cost
    def set_cost(self, cost):
        if self._cleaner_type == "Fast":
            self._cost = 1000
        elif self._cleaner_type == "Large":
            self._cost = 2000
        else:
            self._cost = 500
        if self.get_premium() == True:
            self._cost = self._cost * 10

    def set_clean_area(self, clean_area):
        self._clean_area = clean_area


    def do_task(self):
        self.get_battery()
        self.battery.battery_drain(20)
        if self.get_battery() < 10:
            print(f"{self._name} has blown up due to low battery")
        else:
            print(f"{self._name} is cleaning the area: {self._clean_area}")
            if random.randint(1, 10) >= 80:
                print(f"{self._name} has finished cleaning but now has been lit on fire: {self._clean_area}")
            if random.randint(1, 10) >= 80:
                print(f"{self._name} has finished cleaning: {self._clean_area}")
            self.get_battery()
