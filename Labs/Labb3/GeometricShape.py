import matplotlib.pyplot as plt

def area_comparison(self, other, operator):
    '''Returns True if area comparison is True given the comparison operator'''

    if hasattr(self, 'area') and hasattr(other, 'area'): 
        return True if eval(f'self.area {operator} other.area') else False
    else:
        raise AttributeError('GeometricShape has no attribute "area", only its subclasses') # ändra till "property"?

class GeometricShape:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def translate(self, x, y, z=0):
        '''Plots the object, assigns new x, y and z values, and plots it again.
        If the object has three dimensions, call draw() with translate_values.
        If it has two dimensions, call draw() with translate_axis.
        translate_axis is used to make sure both objects fits the plot'''

        if type(x) in [int, float] and type(y) in [int, float] and type(z) in [int, float]:
            #if isinstance(self, Sphere):
            if z != 0:
                self.draw(translate_values=[x, y, z])
                self.x = x
                self.y = y
                self.z = z
            else:
                self.draw()
                translate_axis = [min(x, self.x) - self.dist_from_center - 5, 
                                max(x, self.x) + self.dist_from_center + 5, 
                                min(y, self.y) - self.dist_from_center - 2.5, 
                                max(y, self.y) + self.dist_from_center + 2.5]
                self.x = x
                self.y = y
                self.z = z
                self.draw(axis=translate_axis)
        else:
            raise ValueError('x, y and z must be numeric')

    def __str__(self):
        return f'GeometricShape centered at x: {self.x}, y: {self.y}, z: {self.z}'
    
    def __repr__(self):
        return f'GeometricShape(x={self.x}, y={self.y}, z={self.z})'
    
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
        '''Set the axis of the plot around axis=[xmin, xmax, ymin, ymax] for two dimensional objects.
        If not given, the axis is calculated based on self.dist_from_center. The y-axis has less 
        length added and subtracted than the x-axis, this is to make both axis have the same rendered length.'''

        try:
            plt.axis(axis) if axis else plt.axis([self.x - self.dist_from_center - 5, 
                                                  self.x + self.dist_from_center + 5, 
                                                  self.y - self.dist_from_center - 2.5, 
                                                  self.y + self.dist_from_center + 2.5])
        except TypeError:
            raise TypeError('axis must be a list: [xmin, xmax, ymin, ymax]')
        except ValueError:
            raise ValueError('axis list must contain only numeric values')