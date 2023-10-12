import math
import numpy as np
import matplotlib.pyplot as plt
import Circle

class Sphere(Circle.Circle):
    def __init__(self, x, y, z, radius):
        super().__init__(x, y, radius)
        self.z = z
        self.volume = (4/3) * math.pi * self.radius ** 3
        self.surface_area = 4 * math.pi ** 2
        self.dist_from_center = 0 # Behövs denna?

    def __str__(self):
        return f'Sphere centered at x: {self.x}, y: {self.y}, z:{self.z} and radius: {self.radius}'
    
    def __repr__(self):
        return f'Sphere(x={self.x}, y={self.y}, z={self.z}, radius={self.radius})'
    
    def is_unit_sphere(self):
        return True if self.radius == 1 and self.x == 0 and self.y == 0 and self.z == 0 else False
    
    def draw(self, axis=[], translate_values=[]):
        '''https://saturncloud.io/blog/rendering-a-3d-sphere-in-matplotlib-a-guide'''

        theta = np.linspace(0, 2.*np.pi, 100)
        phi = np.linspace(0, np.pi, 100)

        # Convert to Cartesian coordinates
        x = self.radius * np.outer(np.cos(theta), np.sin(phi))
        y = self.radius * np.outer(np.sin(theta), np.sin(phi))
        z = self.radius * np.outer(np.ones(np.size(theta)), np.cos(phi))

        # Create a 3D plot
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Plot the sphere
        ax.plot_surface(x + self.x, y + self.y, z + self.z, color='b')
        ax.plot_surface(x + translate_values[0], y + translate_values[1], z + translate_values[2], color='b') if len(translate_values) > 0 else None