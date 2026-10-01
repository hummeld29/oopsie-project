
from random import random

from robot_car import Robotcar
from robot_arm import Robot_dog
from robo_cleaner import cleaner

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
    while True:
        bank_acount = random.randint(10000, 100000)
        print(f"1. buy a Robotcar price is:{el_robo.get_cost()}")
        print(f"2. buy a Robot_dog price is:{el_robo_dogo.get_cost()}")
        print(f"3. buy a premium Robotcar price is:{el_robo.get_cost()}")
        print(f"4. buy a cleaner")
        print(f"5. wait for paycheck")
        print(f"6. Exit")
        print(f"Your bank account balance is: {bank_acount}")
        choice = input("Enter your choice 1, 2, 3, 4, 5, or 6: ")

        if choice == "1":
            bank_acount -= el_robo.get_cost()
            el_robo = Robotcar("", 100, 5000, 6, "driving")
            el_robo.set_name(input("what would you like to name your car? "))
            el_robo.set_passenger_name(input("what would you like to name your passenger? "))
            if input("would you like to set a destination? (y/n) ") == "y":
                el_robo.set_destination(input("what would you like to set your destination to? "))
                el_robo.do_task()
                if input(f"would you like your car to drive right now? (y/n) ") == "y":
                    el_robo.do_task()
                else:
                    break
        elif choice == "2":
            if bank_acount < el_robo_dogo.get_cost():
                print("You don't have enough money to buy this robot.")
            else:
                bank_acount -= el_robo_dogo.get_cost()
                el_robo_dogo = Robot_dog("", 100, 5000, 6, "playing")
                el_robo_dogo.set_name(input("what would you like to name your robo dog? "))
                el_robo_dogo.set_size(input("what size would you like your robot? "))
                if bank_acount < el_robo_dogo.training_cost():
                    print(f"You don't have enough money to train this robot.")
                    if input(f"would you like your dog to play? (y/n) ") == "y":
                        el_robo_dogo.do_task()
                else:
                    if input("would you like your robot to have training? it costs {training_cost} ") == "y":
                        el_robo_dogo.set_training(True)
                        if el_robo_dogo.get_training() == True:

                            el_robo_dogo.do_task()
        elif choice == "4":
                el_robo_cleaner.set_cleaner_type(input("what type of cleaner would you like? The options are 'basic' for 500, 'fast' for 1000, or 'large' for 2000: "))
                if input(f"would you like to buy a premium cleaner? (y/n) ") == "y":
                    el_robo_cleaner.set_premium(True)
                bank_acount -= el_robo_cleaner.get_cost()
                el_robo_cleaner = cleaner("", 100, 5000, 6, "cleaning")
                el_robo_cleaner.set_name(input("what would you like to name your cleaner? "))
                el_robo_cleaner.set_clean_area(input("what area would you like your cleaner to clean? "))
                if input(f"would you like your cleaner to clean right now? (y/n) ") == "y":
                    el_robo_cleaner.do_task()

        elif choice == "5":
            bank_acount += random.randint(1000, 50000)   
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()