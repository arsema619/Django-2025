class Car:
    def __init__(self, make):
        self.make = make

    def get_make(self):
        return self.make

# create object
car1 = Car("Toyota")

# print result
print("Car make:", car1.get_make())
