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
        self.dist_from_center = math.sqrt(self.side1 ** 2 + self.side2 ** 2)

    def __str__(self):
        return f'Rectangle centered at x: {self.x}, y: {self.y} and side1: {self.side1}, side2: {self.side2}'
    
    def __repr__(self):
        return f'Rectangle({self.x}, {self.y}, {self.side1}, {self.side2})'

    def is_square(self):
        return True if self.side1 == self.side2 else False
    
    def draw(self, axis=[]):
        '''Plots the circle based on the given axis. If not given, x and y limits 
        of the plot are calculated based on self.dist_from_center.'''
                
        self.set_axis_for_plot(axis)

        # x and y in plt.Rectangle is its anchor point, bottom left corner. Adjustment is made to make x and y the center.
        rectangle = plt.Rectangle((self.x - self.side1 / 2, self.y - self.side2 / 2), self.side1, self.side2, fill=False)
        plt.gca().add_patch(rectangle)

    def is_inside(self, point):
        '''Returns True if the points x and y values are within the lengths of the
        objects sides, which means the point is inside the objects area.
        point is a tuple with an x and y value (x, y)'''
            
        try:
            return True if self.x - self.side1 / 2 <= point[0] <= self.x + self.side1 / 2 and self.y - self.side2 / 2 <= point[1] <= self.y + self.side2 / 2 else False
        except TypeError:
            raise TypeError('point must be a tuple: (x, y)')
        except ValueError:
            raise ValueError('point tuple nust contain numeric values')
