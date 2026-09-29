from main_robot import Robot
from typing import Literal
from pydantic import BaseModel, ValidationError

class Robot_dog(Robot):
    def __init__(self, name, battery_percent, cost, dof, task, size: Literal["small", "medium", "large", "extra_large"]  ):
        super().__init__(name, battery_percent, cost, dof, task)
        self._size = size
    def get_size(self):
        return self._size
    def set_size(self, size):
        if size not in ["small", "medium", "large", "extra_large"]:
            raise ValueError("Size must be 'small', 'medium', 'large', or 'extra_large'")
        self._size = size
    