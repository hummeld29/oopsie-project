from main_robot import Robot


class RobotArm(Robot):
    def __init__(self, name, battery_percent, cost, dof, task, gripper_type, object_to_grab):
        super().__init__(name, battery_percent, cost, dof, task)
        self._gripper_type = gripper_type
        self._object_to_grab = object_to_grab
    def get_gripper_type(self):
        return self._gripper_type

    def get_object_to_grab(self):
        return self._object_to_grab
    def do_task(self):
        print(f"{self._name} is performing task: {self._task} with {self._gripper_type} to grab {self._object_to_grab}")
       