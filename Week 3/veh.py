class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def info(self):
        print("Brand:", self.brand, "Year:", self.year)

class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model

    def info(self):
        print("Brand:", self.brand, "Year:", self.year, "Model:", self.model)

# test
v = Vehicle("Toyota", 2020)
c = Car("Honda", 2022, "Civic")

v.info()
c.info()
