from main_robot import Robot

class RobotCar(Robot):
    def __init__(self, name, battery_percent, cost, max_speed, task, passenger_name, destination):
        super().__init__(name, battery_percent, cost, max_speed, task)
        self._max_speed = max_speed
        self._passenger_name = passenger_name
        self._destination = destination

    def get_max_speed(self):
        return self._max_speed

    def get_passenger_name(self):
        return self._passenger_name

    def get_destination(self):
        return self._destination

    def do_task(self):
        print(f"{self._name} is driving at maximum speed: {self._max_speed}")
        if random.randint(1, 100) >= 80:
            print(f"{self._name} has crashed into a tree at speed: {self._max_speed}")
            if random.randint(1, 100) >= 80:
                print(f"{self._passenger_name} has died in the crash")
            elif random.randint(1, 100) <= 20:
                print(f"{self._passenger_name} has been mutilated in the crash")
            elif random.randint(1, 100) == 21 :
                print(f"{self._passenger_name} has recived cancer from the litium batteries in the car.")
            else:
                print(f"{self._passenger_name} is safe after the crash")
        else:
            print(f"{self._name} has safely arrived at your destination: {self._destination}")