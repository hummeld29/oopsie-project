


class Robot:
    def __init__(self, name, battery_percent, cost, dof, task):
        self._name = name
        self._battery_percent = battery_percent
        self._cost = cost   
        self._dof = dof
        self._task = task

        list_1_100 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,
        77,
        78,
        79,
        80,
        81,
        82,
        83,
        84,
        85,
        86,
        87,
        88,
        89,
        90,
        91,
        92,
        93,
        94,
        95,
        96,
        97,
        98,
        99,
        100]


    def get_task(self):
        return self._task

    def get_battery(self):
        if self._battery_percent < 0 or self._battery_percent > 100:
            print("Battery percent cannot be above 100 or below 0")
        else:
            return self._battery_percent
        
    def get_dof(self):
        return self._dof if self._dof >= 0 else None

    def get_name(self):
        return self._name

    def get_cost(self):
        return self._cost

    def do_task(self):
        print(f"{self._name} is performing task: {self._task}")