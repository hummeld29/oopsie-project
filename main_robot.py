
import random
import time


def pause(seconds=1.0):
    time.sleep(seconds)


class Battery:
    """
This class acts as a battery to get used by every other class. 
It has multiple functions which are used to drain the battery, set the battery percent, and get the battery percent. 
These functions are used so that the battery can accurately drain battery and track the battery for the other classes.
"""    
    def __init__(self, battery_percent):
        self._battery_percent = battery_percent
    def get_battery_percent(self):
        return self._battery_percent
        
    def set_battery_percent(self, battery_percent):
        if battery_percent < 0 or battery_percent > 100:
            raise ValueError("Battery percent cannot be above 100 or below 0")
        self._battery_percent = battery_percent

    def battery_drain(self, drain_percent):
        if drain_percent < 0 or drain_percent > 100:
            raise ValueError("Drain percent cannot be above 100 or below 0")
        self._battery_percent -= drain_percent
        if self._battery_percent <= 0:
            self._battery_percent = 0
            print("battery has blown up due to low battery")




class Robot:
    """
This class creates a robot that is used in the main loop.
It has attributes for name, battery, cost, dof, and task.
The class has functions to get and set these attributes, as well as a function to perform its task.
This class is also inherited by the RobotCar, Robot_dog, and cleaner classes.
""" 
    def __init__(self, name, battery: Battery, cost, dof, task):
        self._name = name
        if isinstance(battery, Battery):
            self._battery = battery
        else:
            self._battery = Battery(battery)
        self._cost = cost
        self._dof = dof
        self._task = task

    def get_task(self):
        return self._task

    def get_battery(self):
        return self._battery.get_battery_percent()

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
        self._battery.set_battery_percent(battery_percent)


def main():
    from robot_car import RobotCar
    from robot_arm import Robot_dog
    from robo_cleaner import cleaner

    while True:

        el_car = None
        el_dog = None
        el_robo_cleaner = None

        bank_account = random.randint(10000, 100000)

        bad_quality_car = RobotCar("bad quality car", 1, 1000, 2, "driving", "passenger", "destination", None)
        bad_quality_dog = Robot_dog("bad quality dog", 1, 1000, 2, "playing", "small", None, 0)
        bad_quality_cleaner = cleaner("bad quality cleaner", 1, 1000, "cleaning", "small area", False, None, "basic")
        """
This is the main loop of the program. It is where all of the user input is taken and the robots are created and used.
It has a bank account variable that is used to track the user's money.
The user also starts out with bad quality robots and cars that they can use if they don't have enough money to buy a new robot or car.
    """
        print(f"1. buy a Robotcar price varys based on premium features")
        print(f"2. buy a Robot_dog price is based on size and training")
        print(f"3. buy a cleaner robot price is based on type and premium features")
        print(f"4 use your bad quality car/ car that you bought")
        print(f"5 play with your bad quality rob_dog/ dog that you bought")
        print(f"6 use your bad quality cleaner/ cleaner that you bought")
        print(f"7. wait for paycheck")
        print(f"8. Exit")
        print(f"Your bank account balance is: {bank_account}")
        pause(1.5)
        
        choice = input("Enter your choice 1, 2, 3, 4, 5, 6, 7, or 8: ").lower()

        if choice == "1":
            el_car = RobotCar("", 100, 5000, 6, "driving", "passenger", "destination", None)
            wants_premium = input(f"would you like to buy a premium car? (y/n) ").lower() == "y"
            if wants_premium:
                el_car.set_premium(True)

            if bank_account < el_car.get_cost():
                print("You don't have enough money to buy this robot.")
                print(f"Your bank account balance is: {bank_account}")

            else:
                bank_account -= el_car.get_cost()
                el_car.set_name(input("what would you like to name your car? "))
                el_car.set_passenger_name(input("what would you like to name your passenger? "))
                if input("would you like to set a destination? (y/n) ").lower() == "y":
                    el_car.set_destination(input("what would you like to set your destination to? "))
                if input(f"would you like your car to drive right now? (y/n) ").lower() == "y":
                    el_car.do_task()

        elif choice == "2":
            el_dog = Robot_dog("", 100, 5000, 4, "playing", "small", None, 0)

            size_choice = input(
                "What size of dog would you like? ('small', 'medium', 'large', 'extra_large'): ").lower()
            el_dog.set_size(size_choice)

            wants_training = input("Would you like to train your dog? (y/n): ").lower() == "y"
            el_dog.set_training(wants_training)

            total_cost = el_dog.get_cost() + (el_dog.training_cost() if wants_training else 0)

            if bank_account < total_cost:
                if wants_training and bank_account >= el_dog.get_cost():
                    print("You cannot afford the extra training, but you have enough for the dog.")
                    buy_untrained = input("Would you like to buy the dog without training? (y/n): ").lower() == "y"
                    if buy_untrained:
                        el_dog.set_training(False)
                        bank_account -= el_dog.get_cost()
                    else:
                        print("Purchase canceled.")
                        el_dog = None
                else:
                    print("You don't have enough money to buy this robot.")
                    print(f"Your bank account balance is: ${bank_account}")
                    el_dog = None
            else:
                bank_account -= total_cost

            if el_dog is not None:
                el_dog.set_name(input("What would you like to name your dog? "))
                print(f"Congratulations! You bought {el_dog.get_name()}.")

                if input("Would you like your dog to play right now? (y/n): ").lower() == "y":
                    el_dog.do_task()

        elif choice == "3":
            el_robo_cleaner = cleaner("", 100, 5000, "cleaning", "small area", False, None, "basic")
            cleaner_type_choice = input("what type of cleaner would you like? The options are 'basic', 'fast', or 'large': ").lower()
            el_robo_cleaner.set_cleaner_type(cleaner_type_choice)

            would_you_like_premium = input(f"would you like to buy a premium cleaner? (y/n) ").lower() == "y"
            if would_you_like_premium:
                el_robo_cleaner.set_premium(True)

            # FIX (Issue #6): Restructured non-premium path logic so normal cleaners can be successfully purchased and named
            if bank_account < el_robo_cleaner.get_cost():
                print("You don't have enough money to buy this robot.")
                pause(3)
                print(f"Your bank account balance is: {bank_account}")
                el_robo_cleaner = None
            else:
                bank_account -= el_robo_cleaner.get_cost()
                el_robo_cleaner.set_name(input("what would you like to name your cleaner? "))
                if input(f"would you like your cleaner to clean right now? (y/n) ").lower() == "y":
                    el_robo_cleaner.do_task()
                    pause(6)


        elif choice == "4":
            if input(f"would you like your car to drive right now? (good or bad) ").lower() == "good" and el_car is not None:
                el_car.do_task()
                pause(6)
            else:
                bad_quality_car.do_task()
                pause(6)
        elif choice == "5":
            if input(f"would you like your dog to play right now? (good or bad) ").lower() == "good" and el_dog is not None:
                el_dog.do_task()
                pause(6)
            else:
                bad_quality_dog.do_task()
                pause(6)
        elif choice == "6":
            if input(f"would you like your cleaner to clean right now? (good or bad) ").lower() == "good" and el_robo_cleaner is not None:
                el_robo_cleaner.do_task()
                pause(6)
            else:
                bad_quality_cleaner.do_task()
                pause(6)

        elif choice == "7":
            bank_account += random.randint(1000, 50000)
            pause(6)
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please try again.")
            continue
            

if __name__ == "__main__":
    main()
