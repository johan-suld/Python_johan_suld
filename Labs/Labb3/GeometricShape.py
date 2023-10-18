import matplotlib.pyplot as plt
from area_comparison import area_comparison

class GeometricShape:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def translate(self, x, y, z=0):
        '''Plots the object, assigns new x, y and z values, and plots it again.
        translate_values argument of draw() is used for plotting 3d objects, otherwise ignored.
        translate_axis argument of draw() is used for plotting 2d objects, otherwise ignored.
        translate_axis is used to make sure both the original and translated object fits in one plot.'''

        if type(x) in [int, float] and type(y) in [int, float] and type(z) in [int, float]:
            self.draw(translate_values=[x, y, z])

            translate_axis = [min(x, self.x) - self.dist_from_center - 5, 
                            max(x, self.x) + self.dist_from_center + 5, 
                            min(y, self.y) - self.dist_from_center - 2.5, 
                            max(y, self.y) + self.dist_from_center + 2.5]
            
            self.x = x
            self.y = y
            self.z = z

            # 2d objects has no volume attribute, only 2d objects needs draw() to be called 
            # a second time for plotting the translated object.
            if hasattr(self, 'volume') == False:
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
        '''Set the axis of the plot around axis=[xmin, xmax, ymin, ymax] for 2d objects.
        If not given, the axis is calculated based on self.dist_from_center . The y-axis has less 
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