import math
import matplotlib.pyplot as plt
import GeometricShape

class Circle(GeometricShape.GeometricShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius
        self.area = math.pi * radius ** 2
        self.circumference = 2 * math.pi * radius
        self.dist_from_center = radius

    def __str__(self):
        return f'Circle centered at x: {self.x}, y: {self.y} and radius: {self.radius}'
    
    def __repr__(self):
        return f'Circle({self.x}, {self.y}, {self.radius})'

    def is_unit_circle(self):
        return True if self.radius == 1 and self.x == 0 and self.y == 0 else False

    def draw(self, axis=[]):
        self.set_axis_for_plot(axis)

        circle = plt.Circle((self.x, self.y), self.radius, fill=False)
        
        plt.gca().add_patch(circle)

    def is_inside(self, point):
        euclidean_dist = math.sqrt((point[0] - self.x) ** 2 + (point[1] - self.y) ** 2)
        return True if euclidean_dist <= self.radius else False
