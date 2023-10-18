import math
import matplotlib.pyplot as plt
from GeometricShape import GeometricShape

class Circle(GeometricShape):
    def __init__(self, x, y, radius, z=0):
        super().__init__(x, y, z)
        self.radius = radius
        # dist_from center is used to set axis limits of the plots.
        self.dist_from_center = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2
    
    @property
    def circumference(self):
        return 2 * math.pi * self.radius

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, radius):
        if radius <= 0:
            raise ValueError('radius must be greater than 0')
        else:
            self._radius = radius

    def __str__(self):
        return f'Circle centered at x: {self.x}, y: {self.y} and radius: {self.radius}'
    
    def __repr__(self):
        return f'Circle(x={self.x}, y={self.y}, radius={self.radius})'

    def is_unit_circle(self):
        return True if self.radius == 1 and self.x == 0 and self.y == 0 else False

    def draw(self, axis=[], translate_values=[]):
        '''Plots the circle based on axis, it is given if we plot a translated object.
        Otherwise x and y limits of the plot are calculated based on self.dist_from_center .'''

        self.set_axis_for_plot(axis)

        circle = plt.Circle((self.x, self.y), self.radius, fill=False)
        plt.gca().add_patch(circle)

    def is_inside(self, point_x, point_y, point_z=0):
        '''Returns True if the distance from the point and the objects center
        is less than its radius, which means the point is inside the objects area.'''
        
        try:
            # point_z and self.z will bothe be 0 if the object is 2-dimensional.
            euclidean_dist = math.sqrt((point_x - self.x) ** 2 + (point_y - self.y) ** 2 + (point_z - self.z) ** 2)
            return True if euclidean_dist <= self.radius else False
        except ValueError:
            raise ValueError('point_x, point_y and point_z must be numeric')