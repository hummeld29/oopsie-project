import random
from main_robot import Battery
from main_robot import Robot

class RobotCar(Robot):
    """
This classs creates robot cars to be used in the main loop.
It inherits name, battery, cost, dof, and task attributes from the Robot class.
It has extra attributes for max_speed, passenger_name, destination, and premium.
It has functions to get and set these attributes, as well as a function to perform its task.
"""
    def __init__(self, name, battery: Battery, cost, max_speed, task, passenger_name, destination, premium):
        super().__init__(name, battery, cost, max_speed, task)
        self._max_speed = max_speed
        self._passenger_name = passenger_name
        self._destination = destination
        self._premium = premium

    def get_max_speed(self):
        return self._max_speed

    def get_passenger_name(self):
        return self._passenger_name

    def get_destination(self):
        return self._destination

    def get_premium(self):
        return self._premium
    def set_premium(self, premium):
        self._premium = True


    def set_passenger_name(self, passenger_name):
        self._passenger_name = passenger_name

    def set_destination(self, destination):
        self._destination = destination

    def do_task(self):
        print(f"{self._name} is driving at maximum speed: {self._max_speed}")
        
        self._battery.battery_drain(20)
        if self.get_battery() < 10:
            print(f"{self._name} has blown up due to low battery")
            return
        if not self._premium:
        
            if random.randint(1, 100) >= 80:
                print(f"{self._name} has crashed into a tree at speed: {self._max_speed}")
                
                injury_roll = random.randint(1, 100)
                
                if injury_roll >= 80:
                    print(f"{self._passenger_name} has oofed in the crash")
                elif injury_roll <= 20:
                    print(f"{self._passenger_name} has been badly hurt in the crash")
                elif injury_roll == 21:
                    print(f"{self._passenger_name} has received disease from the lithium batteries in the car.")
                else:
                    print(f"{self._passenger_name} is safe after the crash")
                    
            else:
                print(f"{self._name} has safely arrived at your destination: {self._destination}") 
        else:
            print(f"{self._name} has safely arrived at your destination: {self._destination}")
        
