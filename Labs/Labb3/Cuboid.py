import numpy as np
import matplotlib.pyplot as plt
from Rectangle import Rectangle

class Cuboid(Rectangle):
    def __init__(self, x, y, z, side1, side2, side3):
        super().__init__(x, y, side1, side2)
        self.z = z
        self.side3 = side3
        self.volume = side1 * side2 * side3
        self.perimeter = side1 * side2 * 2 + side1 * side3 * 2 + side2 * side3 * 2

    @property
    def side3(self):
        return self._side3
    
    @side3.setter
    def side3(self, side3):
        if side3 <= 0:
            raise ValueError('side3 must be greater than 0')
        else:
            self._side3 = side3

    def __str__(self):
        return f'Cuboid centered at x: {self.x}, y: {self.y}, z: {self.z} and side1: {self.side1}, side2: {self.side2}, side3: {self.side3}'
    
    def __repr__(self):
        return f'Cuboid(x={self.x}, y={self.y}, z={self.z}, side1={self.side1}, side2={self.side2}, side3={self.side3})'

    def is_cube(self):
        return True if self.side1 == self.side2 == self.side3 else False
    
    def draw(self, axis=[], translate_values=[]):
        '''Plots the cuboid, translate_values are used if this function is used to plot a translated cuboid.
        Code for this function is based off the code in this thread:
        https://stackoverflow.com/questions/33540109/plot-surfaces-on-a-cube'''

        def get_cube():   
            phi = np.arange(1,10,2)*np.pi/4
            Phi, Theta = np.meshgrid(phi, phi)

            x = np.cos(Phi)*np.sin(Theta)
            y = np.sin(Phi)*np.sin(Theta)
            z = np.cos(Theta)/np.sqrt(2)
            return x,y,z

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        a = self.side1
        b = self.side2
        c = self.side3
        x,y,z = get_cube()

        # Plot the object
        ax.plot_surface(x*a + self.x, y*b + self.y, z*c + self.z)
        
        # Plot the translated object if there is one
        ax.plot_surface(x*a + translate_values[0], y*a + translate_values[1], z*a + translate_values[2]) if len(translate_values) > 0 else None
