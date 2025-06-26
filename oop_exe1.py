class Circle:
    pi=3.14
    def __init__(self,radius):
        self.radius = radius
    def find_area(self):
        area = self.pi * self.radius * self.radius
        return area
    def find_circumference(self):
        circumference = 2 * self.pi *self.radius
        return circumference

circle = Circle(1000)
print(circle.find_area())
print(circle.find_circumference())


