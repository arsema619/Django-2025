class Animal:
    def make_sound(self):
        print("Animal makes a sound")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

# test
animal = Animal()
cat = Cat()

animal.make_sound()
cat.make_sound()
