from robot_car import Robotcar
from robot_arm import Robot_dog


class Robot:
    def __init__(self, name, battery_percent, cost, dof, task):
        self._name = name
        self._battery_percent = battery_percent
        self._cost = cost
        self._dof = dof
        self._task = task

    def get_task(self):
        return self._task

    def get_battery(self):
        return self._battery_percent

    def get_dof(self):
        return self._dof if self._dof >= 0 else None

    def get_name(self):
        return self._name

    def get_cost(self):
        return self._cost

    def do_task(self):
        print(f"{self._name} is performing task: {self._task}")

    def set_battery(self, battery_percent):
        if battery_percent < 0 or battery_percent > 100:
            raise ValueError("Battery percent cannot be above 100 or below 0")
        self._battery_percent = battery_percent


def main():
    pass