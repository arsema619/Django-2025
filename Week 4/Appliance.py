from abc import ABC, abstractmethod

class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class WashingMachine(Appliance):
    def turn_on(self):
        print("Washing machine is ON")

    def turn_off(self):
        print("Washing machine is OFF")

# test
wm = WashingMachine()
wm.turn_on()
wm.turn_off()
