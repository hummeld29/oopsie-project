from main_robot import Robot

class RobotCar(Robot):
    def __init__(self, name, battery_percent, cost, max_speed, task ):
        super().__init__(name, battery_percent, cost, max_speed, task)
        self._max_speed = max_speed

    def get_max_speed(self):
        return self._max_speed

    def