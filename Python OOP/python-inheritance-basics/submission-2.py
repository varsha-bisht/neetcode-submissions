class SmartDevice:
    def __init__(self, name: str):
        self.name = name

class SmartLight(SmartDevice):
    def turn_on(self):
        print(f"{self.name} is turned on")

    def turn_off(slef):
        print(f"{slef.name} is turned off")


# Don't change the code below
device = SmartLight("Smart Light")
device.turn_on()
device.turn_off()
