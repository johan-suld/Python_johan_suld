import matplotlib.pyplot as plt

def area_comparison(self, other, operator):
    if hasattr(self, 'area') and hasattr(other, 'area'): 
        return 1 if eval(f'self.area {operator} other.area') else 0
    else:
        raise AttributeError('Superclass GeometricShape has no attribute "area", only its subclasses')



class GeometricShape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def translate(self, x, y):
        self.draw()
        translate_axis = [min(x, self.x) - self.dist_from_center - 5, 
                          max(x, self.x) + self.dist_from_center + 5, 
                          min(y, self.y) - self.dist_from_center - 5, 
                          max(y, self.y) + self.dist_from_center + 5]
        self.x = x
        self.y = y
        self.draw(translate_axis)

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
        plt.axis(axis) if axis else plt.axis([self.x - self.dist_from_center - 5, 
                                              self.x + self.dist_from_center + 5, 
                                              self.y - self.dist_from_center - 5, 
                                              self.y + self.dist_from_center + 5])
