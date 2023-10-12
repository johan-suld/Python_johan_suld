import math
import matplotlib.pyplot as plt
import GeometricShape

class Rectangle(GeometricShape.GeometricShape):
    def __init__(self, x, y, side1, side2):
        super().__init__(x, y)
        self.side1 = side1
        self.side2 = side2
        self.area = side1 * side2
        self.circumference = 2 * side1 + 2 * side2
        self.dist_from_center = math.sqrt(self.side1 ** 2 + self.side2 ** 2) / 2

    @property
    def side1(self):
        return self._side1
    
    @side1.setter
    def side1(self, side1):
        if side1 <= 0:
            raise ValueError('side1 must be greater than 0')
        else:
            self._side1 = side1

    @property
    def side2(self):
        return self._side2
    
    @side2.setter
    def side2(self, side2):
        if side2 <= 0:
            raise ValueError('side2 must be greater than 0')
        else:
            self._side2 = side2

    def __str__(self):
        return f'Rectangle centered at x: {self.x}, y: {self.y} and side1: {self.side1}, side2: {self.side2}'
    
    def __repr__(self):
        return f'Rectangle(x={self.x}, y={self.y}, side1={self.side1}, side2={self.side2})'

    def is_square(self):
        return True if self.side1 == self.side2 else False
    
    def draw(self, axis=[]):
        '''Plots the circle based on the given axis. If not given, x and y limits 
        of the plot are calculated based on self.dist_from_center.'''
                
        self.set_axis_for_plot(axis)

        # x and y in plt.Rectangle is its anchor point, bottom left corner. Adjustment is made to make x and y the center.
        rectangle = plt.Rectangle((self.x - self.side1 / 2, self.y - self.side2 / 2), self.side1, self.side2, fill=False)
        plt.gca().add_patch(rectangle)

    def is_inside(self, point_x, point_y, point_z):
        '''Returns True if the points x, y and z values are within the lengths of the
        objects sides, which means the point is inside the objects area.'''
            
        try:
            return True if self.x - self.side1 / 2 <= point_x <= self.x + self.side1 / 2 and self.y - self.side2 / 2 <= point_y <= self.y + self.side2 / 2 and self.z - self.side3 / 2 <= point_z <= self.z + self.side3 / 2 else False
        except ValueError:
            raise ValueError('point_x, point_y and point_z must be numeric')
