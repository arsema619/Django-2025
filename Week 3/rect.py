class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

# create object
rect = Rectangle(5, 4)

# calculate and print area
area = rect.width * rect.height
print("Area:", area)
