import math
import matplotlib.pyplot as plt
import GeometricShape

class Rectangle(GeometricShape):
    def __init__(self, x, y, side1, side2):
        super().__init__(x, y)
        self.side1 = side1
        self.side2 = side2
        self.area = side1 * side2
        self.circumference = 2 * side1 + 2 * side2
        self.dist_from_center = math.sqrt(self.side1 ** 2 + self.side2 ** 2)

    def __str__(self):
        return f'Rectangle centered at x: {self.x}, y: {self.y} and side1: {self.side1}, side2: {self.side2}'
    
    def __repr__(self):
        return f'Rectangle({self.x}, {self.y}, {self.side1}, {self.side2})'

    def is_square(self):
        return True if self.side1 == self.side2 else False
    
    def draw(self, axis=[]):
        self.set_axis_for_plot(axis)

        rectangle = plt.Rectangle((self.x - self.side1 / 2, self.y - self.side2 / 2), self.side1, self.side2, fill=False)
        
        plt.gca().add_patch(rectangle)

    def is_inside(self, point):
        return True if self.x - self.side1 / 2 <= point[0] <= self.x + self.side1 / 2 and self.y - self.side2 / 2 <= point[1] <= self.y + self.side2 / 2 else False
