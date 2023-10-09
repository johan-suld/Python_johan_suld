import matplotlib.pyplot as plt

def area_comparison(self, other, operator):
    '''Returns True if area comparison is True given the comparison operator'''

    if hasattr(self, 'area') and hasattr(other, 'area'): 
        return True if eval(f'self.area {operator} other.area') else False
    else:
        raise AttributeError('Superclass GeometricShape has no attribute "area", only its subclasses')

class GeometricShape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def translate(self, x, y):
        '''Plots the object, assigns new x and y values, and plots it again.
        translate_axis is calculated to make sure both objects fits the plot'''

        if type(x) in [int, float] and type(y) in [int, float]:
            self.draw()
            translate_axis = [min(x, self.x) - self.dist_from_center - 5, 
                              max(x, self.x) + self.dist_from_center + 5, 
                              min(y, self.y) - self.dist_from_center - 2.5, 
                              max(y, self.y) + self.dist_from_center + 2.5]
            self.x = x
            self.y = y
            self.draw(translate_axis)
        else:
            raise ValueError('x and y must be of numeric type')

    def __str__(self):
        return f'GeometricShape centered at x: {self.x}, y: {self.y}'
    
    def __repr__(self):
        return f'GeometricShape({self.x}, {self.y})'
    
    def __eq__(self, other):
        return area_comparison(self, other, '==')

    def __lt__(self, other):
        return area_comparison(self, other, '<')

    def __gt__(self, other):
        return area_comparison(self, other, '>')

    def __le__(self, other):
        return area_comparison(self, other, '<=')

    def __ge__(self, other):
        return area_comparison(self, other, '>=')
    
    def set_axis_for_plot(self, axis):
        '''Set the axis of the plot around axis [xmin, xmax, ymin, ymax]
        If not given, the axis is calculated based on self.dist_from_center.
        The y-axis has less length added and subtracted than the x-axis, this is
        to make both axis have the same rendered length.'''

        try:
            plt.axis(axis) if axis else plt.axis([self.x - self.dist_from_center - 5, 
                                                self.x + self.dist_from_center + 5, 
                                                self.y - self.dist_from_center - 2.5, 
                                                self.y + self.dist_from_center + 2.5])
        except TypeError:
            raise TypeError('axis must be a list: [xmin, xmax, ymin, ymax]')
        except ValueError:
            raise ValueError('axis list nust contain numeric values')