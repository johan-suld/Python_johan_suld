import math
import numpy as np
import matplotlib.pyplot as plt
from Circle import Circle

class Sphere(Circle):
    def __init__(self, x, y, z, radius):
        super().__init__(x, y, radius, z)

    @property
    def volume(self):
        return (4/3) * math.pi * self.radius ** 3
    
    @property
    def surface_area(self):
        return 4 * math.pi * self.radius ** 2

    def __str__(self):
        return f'Sphere centered at x: {self.x}, y: {self.y}, z: {self.z} and radius: {self.radius}'
    
    def __repr__(self):
        return f'Sphere(x={self.x}, y={self.y}, z={self.z}, radius={self.radius})'
    
    def is_unit_sphere(self):
        return True if self.radius == 1 and self.x == 0 and self.y == 0 and self.z == 0 else False
    
    def draw(self, axis=[], translate_values=[]):
        '''Plots the sphere, translate_values are used if this function is used to plot a translated sphere.
        Code for this function is based off the code in this article:
        https://saturncloud.io/blog/rendering-a-3d-sphere-in-matplotlib-a-guide'''

        theta = np.linspace(0, 2.*np.pi, 100)
        phi = np.linspace(0, np.pi, 100)

        x = self.radius * np.outer(np.cos(theta), np.sin(phi))
        y = self.radius * np.outer(np.sin(theta), np.sin(phi))
        z = self.radius * np.outer(np.ones(np.size(theta)), np.cos(phi))

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Plot the object
        ax.plot_surface(x + self.x, y + self.y, z + self.z)

        # Plot the translated object if there is one
        ax.plot_surface(x + translate_values[0], y + translate_values[1], z + translate_values[2]) if len(translate_values) > 0 else None